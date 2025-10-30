# 🤖 Gmail Auto-Reply Bot

An intelligent system for automatically replying to email messages in Gmail, which responds to emails containing specific keywords.

## 🎯 Project Overview

Gmail Auto-Reply Bot is a Python application that connects to your Gmail account, checks for unread messages, and if it finds a predefined keyword in the subject line, automatically sends a pre-written reply.

### Key Features:

- 🔐 Secure connection to the Gmail API using OAuth 2.0
- 📧 Automatic monitoring of unread emails
- 🔑 Sends replies based on keywords in the subject line
- 📝 Customizable reply template
- ❗ Detailed logging for monitoring and debugging
- 💪 Robust error handling during operation

## 🛠️ Technologies & Tools

- **Python 3.8+**
- **Gmail API** - for reading mail and sending replies
- **Google OAuth** - for secure authentication
- **Logging** - for monitoring and debugging

## 📋 System Requirements

- Python 3.8 or higher
- A Google Account
- Gmail API access enabled

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/GmailAutoReply
cd GmailAutoReply
```

### 2. Create a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Google API

#### Enable Two-Factor Authentication:
1. Go to [Google Cloud Console.](https://console.cloud.google.com/)
2. Create a new project and enable the Gmail API.
3. Create OAuth 2.0 Client ID credentials.
4. Download `credentials.json` and place it in the project's root directory.

### 5. Configure the application
Edit the `config.py` file to set the keyword and reply template:
```bash
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
KEYWORD = "doctor"  # Keyword to search for in the email subject
MAILTEMPLATE = "Thank you for your email! We will get back to you shortly." # Reply template
```

## 💻 Usage

### Basic Run:
```bash
python main.py
```

### Project Structure:
```
gmail-auto-reply/
├── main.py              # Main application entry point
├── google_auth.py       # Google authentication module
├── mail_parser.py       # Email parsing module
├── mail_reply.py        # Email reply module
├── logger.py            # Logging configuration
├── config.py            # Script configuration
├── requirements.txt     # Project dependencies
└── logs/                # Logs directory (created automatically)
```

## 📊 Sample Output

<img width="430" height="177" alt="image" src="https://github.com/user-attachments/assets/7857e18c-5191-43cf-a05f-57087c25fcc2" />


## 📝 Logging

All operations are logged to:
- **Console** - basic information and errors
- **Log files** - detailed information in the `logs/` directory

Log file format: `logs_YYYYMMDD.log`

## ⚙️ Configuration

### Configurable parameters in `config.py`:
- `AI_MODEL` - OpenAI model (default: gpt-5-nano)
- `MAILBOX_SELECT` - mailbox to process (default: inbox)
- `MAILS_TO_SEARCH` - type of emails to search for (default: UNSEEN)
- `RESPONSE_FILE` - file to save results

## 🛡️ Security

- Secure OAuth 2.0 is used for API access.
- Secret files (`token.json, credentials.json`) should not be committed to the repository (it is recommended to add them to `.gitignore`).


---

⭐ **If you found this project helpful, please give it a star on GitHub!**
