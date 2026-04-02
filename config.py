#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8724483081:AAEWKmDmF3gBc1zXsJ6H_g3vXjW4gy3pkU8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21750737"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "15fd924a4d5145590b1aaac0b42ff949")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003317447279"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6959898127"))

#Port
PORT = os.environ.get("PORT", "8001")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DATABASE_NAME", "asetnusantarabot")

#force sub channel id, if you want enable force sub  -1003009348872 (DP)
FORCE_SUB_CHANNEL = [-1003791124160,-1003734633464]
try:
    for x in (os.environ.get("FORCE_SUB_CHANNEL", "").split()):
        FORCE_SUB_CHANNEL.append(int(x))
except ValueError:
    raise Exception("Your FORCE_SUB_CHANNEL list does not contain valid integers.")



TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6486738785 8599854604 ").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Halo {first}\n\nNonton full video eksklusif, <b>Wajib Join channel dibawah ini sekarang!</b>")
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(6486738785)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
