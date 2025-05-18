# RAIE-Backend
Recursive AI Executer (Backend)
# Recursive AI Executor — Backend

This is the FastAPI backend for the **Recursive AI Executor**. It provides a single POST endpoint that accepts a natural‑language prompt, uses OpenAI’s GPT to generate Python code, runs that code recursively until it succeeds (or hits a retry limit), and returns the code plus execution logs.

## Prerequisites

- **Python** ≥ 3.9  
- An **OpenAI API key**  
- (Optional) `virtualenv` or `venv`  

---

## Installation

1. Clone this repo (github.com/shivamkumarrai1/RAIE-Backend):

git clone <your-backend-repo-url>
cd backend
        
Install dependencies:

pip install -r requirements.txt

Environment Variables
Create a .env file in the backend/ root with:
OPENAI_API_KEY=sk-…

API Reference:
POST /generate-and-run

Running the Server
Start the FastAPI app on port 8000:

uvicorn main:app --reload --port 8000
The --reload flag auto‑restarts on code changes.

Default URL: http://localhost:8000



Project Structure:

backend/
├── code_runner.py        # runs Python code and returns (success, output)
├── gpt_service.py        # calls OpenAI ChatCompletion to generate code
├── main.py               # FastAPI app with CORS & /generate-and-run
├── requirements.txt
└── .env                  # local OpenAI API key (gitignored)

How It Works->

Receive JSON { prompt } via POST.

Loop up to N retries:

Call generate_code(prompt) → Python script text.

Execute via run_python_code(code) → (success, stdout+stderr).

If failure, append error to prompt and retry.

Return final success flag, code, full output log, and attempt count.

Security & CORS
Uses FastAPI’s CORS middleware to allow only http://localhost:3000.

Sandboxes code execution in a separate process (subprocess)—avoid using exec() directly.

Contributing:

Fork this repo

Create a branch (git checkout -b feature/xyz)

Commit (git commit -m "feat: add xyz")

Push (git push origin feature/xyz)

Open a Pull Request

