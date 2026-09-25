# AI Helpdesk Assistant

A Python-based helpdesk application that helps users troubleshoot common technical issues using a searchable knowledge base and a Streamlit interface.

## Features

* Interactive helpdesk interface
* Knowledge-base based issue retrieval
* MySQL database integration
* Troubleshooting articles for common IT problems
* Offline operation without external API keys
* Streamlit web interface

## Tech Stack

* **Python**
* **Streamlit**
* **MySQL**
* **SQL**
* **Git & GitHub**

## Supported Issues

The knowledge base currently includes troubleshooting information for:

* Wi-Fi connectivity
* VPN issues
* Printer problems
* Email synchronization
* Forgotten passwords
* Slow computers
* Blue-screen errors
* Software installation permissions

## Project Structure

```text
ai-helpdesk-assistant/
│
├── data/
│   └── knowledge_base/
│       ├── bluescreen_error.txt
│       ├── email_not_syncing.txt
│       ├── forgot_password.txt
│       ├── printer_not_printing.txt
│       ├── slow_computer.txt
│       ├── software_install_permission.txt
│       ├── vpn_issues.txt
│       └── wifi_not_connecting.txt
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
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sudiksha2507/ai-helpdesk-assistant.git
cd ai-helpdesk-assistant
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

On Windows, you can also use:

```bash
py -m pip install -r requirements.txt
```

### 3. Set up MySQL

Open MySQL Command Line Client or MySQL Workbench and run:

```sql
SOURCE /path/to/ai-helpdesk-assistant/schema.sql;
```

The application uses the database:

```text
ai_helpdesk_assistant
```

Configure the MySQL connection in:

```text
src/db.py
```

Example:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "appuser",
    "password": "apppass123",
    "database": "ai_helpdesk_assistant"
}
```

### 4. Run the application

From the project folder:

```bash
cd src
```

Then start Streamlit:

```bash
python -m streamlit run app.py
```

Open the application at:

```text
http://localhost:8501
```

## How It Works

1. The user enters a technical problem.
2. The application searches the knowledge base for relevant information.
3. The matching troubleshooting information is displayed to the user.
4. MySQL is used for the application's database functionality.

## Future Improvements

* User authentication
* Helpdesk ticket management
* Conversation history
* Admin dashboard
* Larger knowledge base
* Improved search and retrieval
* Cloud deployment

## Author

**Sudiksha Gopisetty**

GitHub: [Sudiksha2507](https://github.com/Sudiksha2507)
