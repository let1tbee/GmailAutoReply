🤖 Gmail Auto-Reply Bot

An intelligent system for automatically replying to email messages in Gmail, which responds to emails containing specific keywords.

🎯 Project Overview

Gmail Auto-Reply Bot is a Python application that connects to your Gmail account, checks for unread messages, and if it finds a predefined keyword in the subject line, automatically sends a pre-written reply.

Key Features:

    🔐 Secure connection to the Gmail API using OAuth 2.0

    📧 Automatic monitoring of unread emails

    🔑 Sends replies based on keywords in the subject line

    📝 Customizable reply template

    ❗ Detailed logging for monitoring and debugging

    💪 Robust error handling during operation

🛠️ Technologies & Tools

    Python 3.8+

    Gmail API - for reading mail and sending replies

    Google OAuth - for secure authentication

    Logging - for monitoring and debugging

📋 System Requirements

    Python 3.8 or higher

    A Google Account

    Gmail API access enabled

🚀 Installation & Setup

1. Clone the repository

Bash

git clone https://github.com/your-username/GmailAutoReply
cd GmailAutoReply

2. Create a virtual environment

Bash

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

3. Install dependencies

Create a requirements.txt file with the following content:
Plaintext

google-api-python-client
google-auth-httplib2
google-auth-oauthlib

And run the command:
Bash

pip install -r requirements.txt

4. Configure Google API

    Go to the Google Cloud Console.

    Create a new project and enable the Gmail API.

    Create OAuth 2.0 Client ID credentials.

    Download credentials.json and place it in the project's root directory.

5. Configure the application

Edit the config.py file to set the keyword and reply template:
Python

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
KEYWORD = "doctor"  # Keyword to search for in the email subject
MAILTEMPLATE = "Thank you for your email! We will get back to you shortly." # Reply template

💻 Usage

Run the main script. On the first run, you will need to authenticate with Google in your browser.
Bash

python main.py

Project Structure:

gmail-auto-reply/
├── main.py              # Main application entry point
├── google_auth.py       # Google authentication module
├── mail_parser.py       # Email parsing module
├── mail_reply.py        # Email reply module
├── logger.py            # Logging configuration
├── config.py            # Script configuration
├── requirements.txt     # Project dependencies
└── logs/                # Logs directory (created automatically)

📝 Logging

All operations are logged to:

    Console - for basic information and errors

    Log files - for detailed information in the logs/ directory

Log file format: logs_YYYYMMDD.log

🛡️ Security

    Secure OAuth 2.0 is used for API access.

    Secret files (token.json, credentials.json) should not be committed to the repository (it is recommended to add them to .gitignore).

⭐ If you found this project helpful, please give it a star on GitHub!
