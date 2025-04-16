#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "26649585")
API_HASH = os.environ.get("API_HASH", "588a3ea6fd01ae88bd2e10fed7d55b2c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7651012082:AAFVqWXSI3tBaq8igfQehzBNnP9hfCVwhPw")
ADMIN = int(os.environ.get("ADMIN", '7822720438'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "MLTBRM")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "RM_MirrorLeech")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Rahat")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002311502682')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= ""  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '7945551029'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002571138456)
