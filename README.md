# AI Helpdesk Assistant

A Python-based helpdesk application that helps users troubleshoot common technical issues using a knowledge base and optional Gemini-powered responses.

## Features

- Interactive helpdesk interface
- Knowledge-base based issue retrieval
- Optional Google Gemini integration
- MySQL database integration
- Troubleshooting knowledge base
- Offline fallback without an API key
- Streamlit web interface

## Tech Stack

- Python
- Streamlit
- MySQL
- SQL
- Google Gemini API
- Git & GitHub

## How It Works

User Question
↓
Streamlit Interface
↓
Knowledge Base Retrieval
↓
Relevant Troubleshooting Information
↓
AI-generated response or knowledge-base response

The application searches the knowledge base for information related to the user's problem.

If a Gemini API key is configured, the retrieved information can be used to generate a more conversational response. Otherwise, the application uses the knowledge-base response directly.

## Supported Issues

- Wi-Fi connectivity
- VPN issues
- Printer problems
- Email synchronization
- Forgotten passwords
- Slow computers
- Blue-screen errors
- Software installation permissions

## Project Structure

ai-helpdesk-assistant/
│
├── data/
│   └── knowledge_base/
│
├── src/
│   ├── app.py
│   ├── db.py
│   ├── llm_client.py
│   └── retrieval.py
│
├── schema.sql
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## Setup

### 1. Clone the repository

git clone https://github.com/Sudiksha2507/ai-helpdesk-assistant.git

cd ai-helpdesk-assistant

### 2. Install dependencies

python -m pip install -r requirements.txt

On Windows, you can also use:

py -m pip install -r requirements.txt

### 3. Set up MySQL

Open MySQL and run the schema.sql file.

The application uses the database:

ai_helpdesk_assistant

Configure your MySQL credentials in:

src/db.py

Example:

DB_CONFIG = {
    "host": "localhost",
    "user": "appuser",
    "password": "apppass123",
    "database": "ai_helpdesk_assistant"
}

### 4. Optional Gemini API

The application works without Gemini using the knowledge-base fallback.

To enable AI-generated responses, set the GEMINI_API_KEY environment variable.

Windows Command Prompt:

set GEMINI_API_KEY=your-api-key

Windows PowerShell:

$env:GEMINI_API_KEY="your-api-key"

Never commit your actual API key to GitHub.

### 5. Run the application

cd src

python -m streamlit run app.py

Open:

http://localhost:8501

## Future Improvements

- User authentication
- Helpdesk ticket management
- Conversation history
- Admin dashboard
- Larger knowledge base
- Improved semantic search
- Cloud deployment

## Author

Sudiksha Gopisetty

GitHub: https://github.com/Sudiksha2507