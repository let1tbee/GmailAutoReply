from google_auth import google_auth
from logger import get_logger
from mail_parser import mail_parser

logger = get_logger(__name__)

def main():
    logger.info('Script started')
    creds = google_auth()
    mail_parser(creds)
    logger.info('Script successfully finished')

if __name__ == '__main__':
    main()