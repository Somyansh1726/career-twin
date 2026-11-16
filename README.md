# Local AI Career Twin

A local AI-powered professional assistant built with Python, Ollama and the OpenAI-compatible API.

Career Twin uses a professional profile as context to answer questions about education, technical skills, work experience and projects.

The goal of this project is to explore how LLM-powered applications can use personal context while minimizing unsupported claims.

## Features

- Interactive command-line interface.
- Local LLM inference using Ollama.
- Professional profile loading from Markdown.
- Context-aware responses using system and user messages.
- Basic safeguards against invented qualifications and experience.
- No paid OpenAI API key required.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Ollama | Local LLM inference |
| Llama 3.2 3B | Language model |
| OpenAI Python SDK | API-compatible client |
| uv | Dependency and environment management |

## Project Structure

```text
career-twin/
├── main.py
├── profile.md
├── profile.example.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

`profile.md` contains the user's private information and is intentionally excluded from Git.

## Setup

### 1. Install prerequisites

Install:
- Python 3.12 or later
- uv
- Ollama

### 2. Download the model

```powershell
ollama pull llama3.2:3b
```

Make sure Ollama is running locally.

### 3. Clone the repository

```powershell
git clone YOUR_REPOSITORY_URL
cd career-twin
```

### 4. Install Python dependencies

```powershell
uv sync
```

### 5. Create your professional profile

```powershell
Copy-Item profile.example.md profile.md
```

Edit `profile.md` with your own professional information.

Do not upload this private file to a public repository.

### 6. Run the application

```powershell
uv run python main.py
```

Type `exit` to close the application.

## Example Questions

- What technologies have I used?
- Explain my latest project.
- Summarize my professional experience.
- What machine learning techniques have I worked with?

## Current Limitations

- Response quality depends on the local model.
- LLM responses may still contain inaccurate information.
- The application currently supplies the complete profile as context for each question.
- No retrieval-augmented generation (RAG) or persistent conversation memory is implemented yet.
- This is an educational prototype, not a production-ready recruitment system.

## Future Improvements

- Better factual retrieval from professional documents.
- Automated response evaluation.
- Unit testing and error handling.
- Improved conversation history.
- Web-based user interface.
- More reliable model selection and configuration.

## Learning Goals

This project is part of my practical learning journey in Python, local LLM integration and AI application development.