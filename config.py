#(©)CodeXBotz

import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables dari file .env
load_dotenv()


# ============================
# Konfigurasi Wajib (Required)
# ============================

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
if not TG_BOT_TOKEN:
    raise ValueError("TG_BOT_TOKEN belum diset! Silakan isi di file .env")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "0"))
if APP_ID == 0:
    raise ValueError("APP_ID belum diset! Silakan isi di file .env")

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")
if not API_HASH:
    raise ValueError("API_HASH belum diset! Silakan isi di file .env")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))
if CHANNEL_ID == 0:
    raise ValueError("CHANNEL_ID belum diset! Silakan isi di file .env")

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
if OWNER_ID == 0:
    raise ValueError("OWNER_ID belum diset! Silakan isi di file .env")


# ============================
# Konfigurasi Opsional
# ============================

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharingbot")

# Force sub channel IDs (comma-separated di .env)
# Contoh di .env: FORCE_SUB_CHANNEL=-1003791124160,-1003734633464
FORCE_SUB_CHANNEL = [
    int(x.strip()) for x in os.environ.get("FORCE_SUB_CHANNEL", "").split(",") if x.strip()
]

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link."
)

# Admins (space-separated di .env)
try:
    ADMINS = []
    for x in os.environ.get("ADMINS", "").split():
        ADMINS.append(int(x))
except ValueError:
    raise ValueError("ADMINS list di .env harus berisi angka yang valid (pisahkan dengan spasi).")

# Force sub message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {first}\n\n<b>Wajib Join channel dibawah ini!</b>"
)

# Custom Caption (None = disable)
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Protect content (prevent forwarding)
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "True") == "True" else False

# Disable channel share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

BOT_STATS_TEXT = os.environ.get("BOT_STATS_TEXT", "<b>BOT UPTIME</b>\n{uptime}")
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "❌Don't send me messages directly I'm only File Share bot!")

# Tambahkan OWNER_ID ke ADMINS jika belum ada
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)


# ============================
# Logging
# ============================

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