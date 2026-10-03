import motor.motor_asyncio
from config import MONGO_DB_URI, DEFAULT_LANG, DEFAULT_PLAY_MODE

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
db = mongo_client["VaniMusicDB"]
chats_db = db["chats"]

DEFAULT_SETTINGS = {
    "language": DEFAULT_LANG,
    "play_mode": DEFAULT_PLAY_MODE,   # "user" or "admin"
    "auth_users": [],
    "vclogger": False,
}


async def get_chat_settings(chat_id: int) -> dict:
    chat = await chats_db.find_one({"chat_id": chat_id})
    if not chat:
        settings = DEFAULT_SETTINGS.copy()
        settings["chat_id"] = chat_id
        await chats_db.insert_one(settings)
        return settings
    return chat


# ---------------- Language ----------------
async def get_language(chat_id: int) -> str:
    chat = await get_chat_settings(chat_id)
    return chat.get("language", DEFAULT_LANG)


async def set_language(chat_id: int, lang: str):
    await chats_db.update_one(
        {"chat_id": chat_id}, {"$set": {"language": lang}}, upsert=True
    )


# ---------------- Play Permission Mode ----------------
async def get_play_mode(chat_id: int) -> str:
    chat = await get_chat_settings(chat_id)
    return chat.get("play_mode", DEFAULT_PLAY_MODE)


async def set_play_mode(chat_id: int, mode: str):
    await chats_db.update_one(
        {"chat_id": chat_id}, {"$set": {"play_mode": mode}}, upsert=True
    )


# ---------------- Authorized Users (for Admin Mode) ----------------
async def get_auth_users(chat_id: int) -> list:
    chat = await get_chat_settings(chat_id)
    return chat.get("auth_users", [])


async def add_auth_user(chat_id: int, user_id: int):
    await chats_db.update_one(
        {"chat_id": chat_id}, {"$addToSet": {"auth_users": user_id}}, upsert=True
    )


async def remove_auth_user(chat_id: int, user_id: int):
    await chats_db.update_one(
        {"chat_id": chat_id}, {"$pull": {"auth_users": user_id}}
    )


# ---------------- VC Logger toggle ----------------
async def get_vclogger(chat_id: int) -> bool:
    chat = await get_chat_settings(chat_id)
    return chat.get("vclogger", False)


async def set_vclogger(chat_id: int, value: bool):
    await chats_db.update_one(
        {"chat_id": chat_id}, {"$set": {"vclogger": value}}, upsert=True
    )


# ---------------- Utility ----------------
async def get_all_chats() -> list:
    chats = []
    async for chat in chats_db.find({}):
        chats.append(chat["chat_id"])
    return chats
