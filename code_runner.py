import subprocess

def run_python_code(code):
    try:
        with open("temp.py", "w") as f:
            f.write(code)
        result = subprocess.run(
            ["python", "temp.py"],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)
