# agentic_learning

## LangChain beginner setup

This project includes a beginner LangChain script that answers:
`What is the capital of India`

### 1) Install Python (if not installed)
Install Python 3.11+ (recommended) from: https://www.python.org/downloads/ or use the Docker instructions below to run with `python:latest`.

### 2) Create and activate virtual environment (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies
```powershell
pip install -r requirements.txt
```

### 4) Set your OpenAI API key
```powershell
Copy-Item .env.example .env
```
Then open `.env` and replace the key value with your `OPENAI_API_KEY`.

### Optional: Run with Docker (uses latest Python image)
Build the image:
```powershell
docker build -t agentic_learning:latest .
```
Run the container (mounting current folder and env):
```powershell
docker run --rm -v ${PWD}:/app --env-file .env agentic_learning:latest
```

### 5) Run the program
```powershell
python main.py
```

Expected answer should include: `New Delhi`.
