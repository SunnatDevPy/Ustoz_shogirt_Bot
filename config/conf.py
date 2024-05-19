import os

from dotenv import load_dotenv

load_dotenv()


class DB:
    pass


class BOT_CONFIG:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    ADMIN_ID = os.getenv('ADMIN_ID')

