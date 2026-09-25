# \# AI Helpdesk Assistant

# 

# An AI-powered helpdesk application that helps users troubleshoot common technical issues using a searchable knowledge base and optional Gemini-powered response generation.

# 

# The application provides a simple Streamlit interface where users can describe their technical problem and receive a relevant solution from the project's knowledge base.

# 

# \## Features

# 

# \* 💬 Simple helpdesk chat interface

# \* 🔎 Knowledge-base retrieval for common technical issues

# \* 🤖 Optional AI-generated responses using Google Gemini

# \* 🗄️ MySQL database integration

# \* 📚 Pre-built troubleshooting articles

# \* 🔐 Environment-variable based API key configuration

# \* ⚡ Offline fallback when an LLM API key is not configured

# \* 🌐 Streamlit web interface

# 

# \## Tech Stack

# 

# | Technology            | Purpose                         |

# | --------------------- | ------------------------------- |

# | \*\*Python\*\*            | Application backend             |

# | \*\*Streamlit\*\*         | Web interface                   |

# | \*\*MySQL\*\*             | Database                        |

# | \*\*SQL\*\*               | Database schema and queries     |

# | \*\*Google Gemini API\*\* | Optional AI-generated responses |

# | \*\*Git \& GitHub\*\*      | Version control                 |

# 

# \## How It Works

# 

# The application follows a simple helpdesk workflow:

# 

# ```text

# User Question

# &#x20;    │

# &#x20;    ▼

# Streamlit Interface

# &#x20;    │

# &#x20;    ▼

# Knowledge Base Retrieval

# &#x20;    │

# &#x20;    ▼

# Relevant Troubleshooting Article

# &#x20;    │

# &#x20;    ├── Gemini API configured

# &#x20;    │        │

# &#x20;    │        ▼

# &#x20;    │   AI-generated response

# &#x20;    │

# &#x20;    └── Gemini API not configured

# &#x20;             │

# &#x20;             ▼

# &#x20;      Knowledge-base response

# ```

# 

# The retrieval component searches the available troubleshooting articles and identifies relevant information for the user's query.

# 

# When a Gemini API key is configured, the retrieved information can be used to generate a more natural response. Without an API key, the application continues to work using the knowledge-base fallback.

# 

# \## Project Structure

# 

# ```text

# ai-helpdesk-assistant/

# │

# ├── data/

# │   └── knowledge\_base/

# │       ├── bluescreen\_error.txt

# │       ├── email\_not\_syncing.txt

# │       ├── forgot\_password.txt

# │       ├── printer\_not\_printing.txt

# │       ├── slow\_computer.txt

# │       ├── software\_install\_permission.txt

# │       ├── vpn\_issues.txt

# │       └── wifi\_not\_connecting.txt

# │

# ├── src/

# │   ├── app.py

# │   ├── db.py

# │   ├── llm\_client.py

# │   └── retrieval.py

# │

# ├── .env.example

# ├── .gitignore

# ├── requirements.txt

# ├── schema.sql

# └── README.md

# ```

# 

# \## Supported Issues

# 

# The included knowledge base currently contains troubleshooting information for issues such as:

# 

# \* Wi-Fi connectivity problems

# \* VPN issues

# \* Printer problems

# \* Email synchronization

# \* Forgotten passwords

# \* Slow computers

# \* Blue-screen errors

# \* Software installation permissions

# 

# \## Requirements

# 

# Before running the project, install:

# 

# \* Python 3

# \* MySQL Server

# \* Git

# 

# \## Installation

# 

# \### 1. Clone the Repository

# 

# ```bash

# git clone https://github.com/Sudiksha2507/ai-helpdesk-assistant.git

# cd ai-helpdesk-assistant

# ```

# 

# \### 2. Install Dependencies

# 

# ```bash

# python -m pip install -r requirements.txt

# ```

# 

# If `python` is not recognized on Windows, try:

# 

# ```bash

# py -m pip install -r requirements.txt

# ```

# 

# \## Database Setup

# 

# Make sure MySQL Server is running.

# 

# Open \*\*MySQL Command Line Client\*\* or \*\*MySQL Workbench\*\* and run the project schema:

# 

# ```sql

# SOURCE /path/to/ai-helpdesk-assistant/schema.sql;

# ```

# 

# The application uses the following database:

# 

# ```text

# ai\_helpdesk\_assistant

# ```

# 

# \### Database User

# 

# The application can use a MySQL user such as:

# 

# ```text

# Username: appuser

# Password: apppass123

# ```

# 

# If the user does not already exist:

# 

# ```sql

# CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'apppass123';

# ```

# 

# Grant database access:

# 

# ```sql

# GRANT ALL PRIVILEGES

# ON ai\_helpdesk\_assistant.\*

# TO 'appuser'@'localhost';

# 

# FLUSH PRIVILEGES;

# ```

# 

# > For a real deployment, use a strong password instead of the example credentials above.

# 

# \## Database Configuration

# 

# Open:

# 

# ```text

# src/db.py

# ```

# 

# Configure the database connection according to your local MySQL setup:

# 

# ```python

# DB\_CONFIG = {

# &#x20;   "host": "localhost",

# &#x20;   "user": "appuser",

# &#x20;   "password": "apppass123",

# &#x20;   "database": "ai\_helpdesk\_assistant"

# }

# ```

# 

# \## Optional Gemini API Configuration

# 

# The application can run without a Gemini API key using the knowledge-base fallback.

# 

# To enable AI-generated responses, create an API key and set the `GEMINI\_API\_KEY` environment variable.

# 

# \### Windows Command Prompt

# 

# ```cmd

# set GEMINI\_API\_KEY=your-api-key

# ```

# 

# \### Windows PowerShell

# 

# ```powershell

# $env:GEMINI\_API\_KEY="your-api-key"

# ```

# 

# The project includes:

# 

# ```text

# .env.example

# ```

# 

# as a configuration reference.

# 

# \*\*Never commit your actual API key to GitHub.\*\*

# 

# \## Running the Application

# 

# Navigate to the `src` directory:

# 

# ```bash

# cd src

# ```

# 

# Start the Streamlit application:

# 

# ```bash

# python -m streamlit run app.py

# ```

# 

# The application will normally be available at:

# 

# ```text

# http://localhost:8501

# ```

# 

# \## Example Workflow

# 

# A user can enter a problem such as:

# 

# ```text

# My Wi-Fi is connected but I cannot access the internet.

# ```

# 

# The application searches the knowledge base for relevant troubleshooting information and returns an appropriate solution.

# 

# If Gemini is configured, the retrieved information can additionally be used to generate a conversational response.

# 

# \## Error Handling

# 

# The application is designed to continue functioning even when the optional Gemini API is not configured.

# 

# This allows the project to be tested locally using the included knowledge base without requiring an external AI service.

# 

# \## Future Improvements

# 

# Possible improvements include:

# 

# \* User authentication

# \* Helpdesk ticket creation and tracking

# \* Conversation history

# \* Admin dashboard

# \* Larger knowledge base

# \* Better semantic search

# \* Ticket status management

# \* User feedback and solution ratings

# \* Cloud deployment

# \* More advanced AI-powered troubleshooting

# 

# \## Learning Outcomes

# 

# This project demonstrates practical experience with:

# 

# \* Python application development

# \* Streamlit web applications

# \* MySQL database connectivity

# \* SQL database design

# \* Retrieval-based information systems

# \* API integration

# \* Environment variables

# \* Git and GitHub

# \* Basic application architecture

# 

# \## Author

# 

# \*\*Sudiksha Gopisetty\*\*

# 

# GitHub: \[Sudiksha2507](https://github.com/Sudiksha2507)

# 

# \---

# 

# ⭐ If you found this project useful, feel free to explore the repository and build upon it.



