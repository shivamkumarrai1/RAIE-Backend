import os
import json
import requests
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from code_runner import run_python_code

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                  "https://raie-frontend.vercel.app"
                  ],
    allow_credentials=True,
    allow_methods=["*"],   # THIS IS IMPORTANT
    allow_headers=["*"],
)

@app.post("/generate-and-run")
async def generate_and_run(data: dict):
    prompt = data.get("prompt", "")
    max_retries = 5
    attempts = 0
    output_log = ""

    api_key = os.getenv("OPENAI_API_KEY")

    while attempts < max_retries:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer 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",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "mistralai/mistral-7b-instruct",
                    "messages": [
                        {
                            "role": "system",
                            "content": "Generate a correct and runnable Python script."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                }
            )

            result = response.json()

            if "error" in result:
                return {"success": False, "error": result}

            code = result["choices"][0]["message"]["content"]

            success, output = run_python_code(code)

            output_log += f"\n\nAttempt {attempts + 1}:\n{code}\n{output}"

            if success:
                return {
                    "success": True,
                    "code": code,
                    "output": output_log,
                    "attempts": attempts + 1
                }
            else:
                prompt += f"\n\nFix the error: {output}"
                attempts += 1

        except Exception as e:
            return {
                "success": False,
                "code": "",
                "output": str(e),
                "attempts": attempts + 1
            }

    return {
        "success": False,
        "code": "",
        "output": output_log,
        "attempts": attempts

    }
