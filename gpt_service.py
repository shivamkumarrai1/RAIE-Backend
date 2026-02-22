import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
async def generate_code(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",  # OpenRouter model naming format
        messages=[
            {"role": "system", "content": "Generate a correct and runnable Python script."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()