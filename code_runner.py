import subprocess

def extract_code(content):
    """
    Extract the actual Python code from the content.
    Assumes the code is enclosed within triple backticks (```).
    """
    lines = content.splitlines()
    code_lines = []
    inside_code_block = False

    for line in lines:
        # Detect the start and end of the code block
        if line.strip() == "```python":
            inside_code_block = True
            continue
        elif line.strip() == "```":
            inside_code_block = False
            continue

        # Collect lines inside the code block
        if inside_code_block:
            code_lines.append(line)

    return "\n".join(code_lines)

def run_python_code(code):
    print("Original Code:", code)
    try:
        # Extract only the actual Python code
        extracted_code = extract_code(code)
        print("Extracted Code:", extracted_code)

        # Write the extracted code to temp.py
        with open("temp.py", "w") as f:
            f.write(extracted_code)

        # Run the temp.py file
        result = subprocess.run(
            ["C:\\Users\\shivam\\AppData\\Local\\Programs\\Python\\Python312\\python.exe", "temp.py"],
            capture_output=True,
            text=True, 
            timeout=5
        )
        output = result.stdout + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)
