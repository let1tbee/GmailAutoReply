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
- **OpenAI API** - for text analysis
- **IMAP/Gmail API** - for email retrieval
- **python-dotenv** - for configuration management
- **Logging** - for monitoring and debugging

## 📋 System Requirements

- Python 3.8 or higher
- Gmail account with two-factor authentication enabled
- OpenAI API key
- Gmail app password

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/let1tbee/Email-Assistant
cd Email-Assistant
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

### 4. Configure environment variables
Create a `.env` file based on the `.env.example`:

```bash
cp .env.example .env
```

Fill in your `.env` file with your credentials:
```env
GMAIL_EMAIL=your-email@gmail.com
GMAIL_PASSWORD=your-app-password
OPENAI_API_KEY=your-openai-api-key
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
```

### 5. Gmail Setup

#### Enable Two-Factor Authentication:
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Select "Security" → "2-Step Verification"
3. Enable two-factor authentication

#### Create App Password:
1. In the "Security" section, select "App passwords"
2. Select "Mail" and your operating system
3. Copy the generated password to the `GMAIL_PASSWORD` variable

### 6. Get OpenAI API Key
1. Register on [OpenAI Platform](https://platform.openai.com/)
2. Navigate to API Keys section
3. Create a new API key
4. Copy the key to the `OPENAI_API_KEY` variable

## 💻 Usage

### Basic Run:
```bash
python main.py
```

### Project Structure:
```
ai-email-analyzer/
├── main.py              # Main application file
├── mails_handler.py     # Email processing module
├── openAI_handler.py    # OpenAI integration module
├── utils.py             # Utility functions
├── logger.py            # Logging configuration
├── config.py            # Application configuration
├── requirements.txt     # Project dependencies
├── .env.example         # Environment variables example
├── .gitignore           # Git ignore file
└── logs/                # Logs directory (created automatically)
```

## 📊 Sample Output

The application generates an `output.txt` file with analysis results:

```
Main Points from Emails:
• Meeting scheduled for tomorrow at 2 PM
• Budget report needs review by Friday
• New project requirements received

Action Items:
• Prepare presentation materials for tomorrow's meeting
• Review and approve Q3 budget report
• Schedule call with client to discuss new requirements
• Send confirmation email for meeting attendance
```

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

- All sensitive data is stored in the `.env` file
- The `.env` file is added to `.gitignore`
- SSL connection is used for IMAP
- API keys are not stored in the code


## ❗ Limitations

- Maximum 5 emails per run (API token limitation)
- Only Gmail IMAP is supported
- Only unread emails are analyzed
- Requires active internet connection

---

⭐ **If you found this project helpful, please give it a star on GitHub!**
