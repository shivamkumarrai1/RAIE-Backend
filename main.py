from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gpt_service import generate_code
from code_runner import run_python_code

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # <-- array, not a single string
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/ping")
def ping():
    return {"msg": "pong"}


@app.post("/generate-and-run")
async def generate_and_run(data: dict):
    prompt = data.get("prompt", "")
    max_retries = 5
    attempts = 0
    output_log = ""
    
    while attempts < max_retries:
        code = await generate_code(prompt)
        success, output = run_python_code(code)
        output_log += f"\n\nAttempt {attempts + 1}:\n{code}\n{output}"
        if success:
            return {"success": True, "code": code, "output": output_log, "attempts": attempts + 1}
        else:
            prompt += f"\n\nFix the error: {output}"
            attempts += 1

    return {"success": False, "code": code, "output": output_log, "attempts": attempts}
