import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_code(prompt):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generate a correct and runnable Python script."},
            {"role": "user", "content": prompt}
        ]
    )
    return res['choices'][0]['message']['content'].strip()

