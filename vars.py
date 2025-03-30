# Don't Remove Credit Tg - @Tushar0125
# Ask Doubt on telegram @Tushar0125

from os import environ

API_ID = int(environ.get("API_ID", "28206084"))
API_HASH = environ.get("API_HASH", "6b56f4cc8ef5750f51616cc22b78168d")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

  AUTH_USER = os.environ.get("AUTH_USERS", "1110590703").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    
