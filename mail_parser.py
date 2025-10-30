from mail_reply import mail_reply

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import KEYWORD
from logger import get_logger

logger = get_logger(__name__)

def mail_parser(creds):
    """
       Checks unread messages. If there are keyword in subject of unread messages - calls mail_reply sunction

       Args:
           creds: Credentials object
       """
    logger.info('Parsing unread mails')
    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = (
            service.users().messages().list(userId="me", labelIds=["UNREAD","CATEGORY_PERSONAL"]).execute()
        )
        messages = results.get("messages", [])

        if not messages:
            logger.info('No unread messages')
            return

        logger.info('Messages found: ')
        for message in messages:
            msg = (
                service.users().messages().get(userId="me", id=message["id"]).execute()
            )
            message_content = msg.get("payload", {}).get("headers")
            thread_id = message["threadId"]
            for name in message_content:
                if name.get("name") == "From":
                    receiver = name.get("value")
                if name.get("name") == "Message-ID":
                    references = name.get("value")
                if name.get("name") == "Subject":
                    if name.get("value").lower().count(KEYWORD) > 0:
                        logger.info(f'Mails with keywords found: {name.get("value")}')
                        mail_reply(message["id"], receiver, references, name.get("value"), service, thread_id)

    except HttpError as error:
        logger.warning(f"An error occurred during parsing mails: {error}")