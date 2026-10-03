import os

# ==== Telegram Bot Credentials ====
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# ==== Assistant Account (userbot) ====
# Generate this with a "string session generator" script (Pyrogram).
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# ==== Database ====
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb://localhost:27017")

# ==== Owner / Admin ====
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

# ==== Logger group where /vclogger events get sent (optional) ====
LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID", "0"))

# ==== Branding ====
BOT_NAME = os.environ.get("BOT_NAME", "Vani X Music")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "your_bot_username")
START_IMG = os.environ.get(
    "START_IMG",
    "https://telegra.ph/file/example-start-image.jpg",
)
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "https://t.me/YourSupportChat")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/YourUpdatesChannel")

# ==== Defaults ====
DEFAULT_LANG = "en"
DEFAULT_PLAY_MODE = "user"  # "user" or "admin"

# ==== Download folder ====
DOWNLOADS_DIR = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)
