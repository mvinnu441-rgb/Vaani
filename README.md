# 🎵 Vani X Music — Telegram Voice Chat Music Bot

A complete Telegram group voice-chat music bot built with **Pyrogram** +
**PyTgCalls**. Streams songs and videos into group voice chats, with a
button-driven help menu, per-group play permissions, and English/Hindi
language support.

## ✨ Features

- `/start`, `/help` — rich welcome + interactive button-based help menu
- `/play`, `/vplay` — stream audio / video into the voice chat
- `/pause`, `/resume`, `/skip`, `/end`, `/queue`, `/loop`
- `/lang` — switch between English 🇬🇧 and Hindi 🇮🇳 (only these two)
- `/reload`, `/reboot` (owner only)
- `/vclogger` — toggle voice-chat activity logging
- `/ping` — check bot latency
- **Play Permission Mode**: `User Mode` (anyone can play) or
  `Admin Mode` (only admins / `/authuser`-authorized members can play)
- `/authuser`, `/unauthuser` — manage authorized users in Admin Mode
- Auto "No active voice chat found" message if `/play` is used with no VC
- Now-playing card with inline **Pause / Resume / Skip** buttons
- Auto "Stream has ended" message + auto-advance to next queued track
- Detailed welcome message when added to a new group (added by, chat ID, etc.)

## 📁 Project Structure

```
vani-music-bot/
├── main.py                     # entry point
├── config.py                   # env var config
├── requirements.txt
├── Procfile
├── runtime.txt
├── sample.env                  # rename to .env and fill in
├── string_session_generator.py # generates STRING_SESSION
├── database/
│   └── db.py                   # MongoDB (language, play mode, auth users)
├── helpers/
│   ├── language.py              # English + Hindi strings
│   ├── decorators.py            # permission checks
│   ├── queue.py                  # per-chat queue manager
│   ├── ytdl.py                    # yt-dlp search/download
│   └── calls.py                    # pytgcalls wrapper
└── plugins/
    ├── start.py       # /start /help
    ├── play.py         # /play /vplay
    ├── controls.py      # /pause /resume /skip /end /queue /loop
    ├── settings.py       # /lang /settings /authuser /unauthuser
    ├── misc.py             # /ping /reload /reboot /vclogger
    ├── welcome.py           # group-join welcome message
    └── callbacks.py          # inline button handlers
```

## ⚙️ Required Credentials

| Variable | Where to get it |
|---|---|
| `API_ID`, `API_HASH` | https://my.telegram.org |
| `BOT_TOKEN` | [@BotFather](https://t.me/BotFather) |
| `STRING_SESSION` | Run `string_session_generator.py` (see below) |
| `MONGO_DB_URI` | Free cluster at [MongoDB Atlas](https://www.mongodb.com/atlas) |
| `OWNER_ID` | Your numeric Telegram user ID (e.g. via [@userinfobot](https://t.me/userinfobot)) |
| `START_IMG` | A direct image URL for the bot's start/help banner |

## 🚀 Local Setup

1. **Clone this repo** (after uploading it to your own GitHub):
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd vani-music-bot
   ```

2. **Install system dependency FFmpeg** (required for audio/video streaming):
   ```bash
   sudo apt update && sudo apt install ffmpeg -y
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate your assistant's STRING_SESSION:**
   ```bash
   python3 string_session_generator.py
   ```
   Log in with the *personal account* that should join voice chats (not
   the bot token). Copy the string it prints out.

5. **Configure environment variables:**
   Copy `sample.env` to `.env` and fill in every value, **or** set the
   same variables directly in your hosting platform's dashboard
   (Heroku/Railway/VPS).

6. **Run the bot:**
   ```bash
   python3 main.py
   ```

## ☁️ Deploying from GitHub

- **Heroku / Railway**: connect your GitHub repo, set all variables from
  `sample.env` as Config Vars / Environment Variables, deploy — the
  included `Procfile` and `runtime.txt` handle the rest.
- **VPS (Ubuntu)**: clone the repo, follow the *Local Setup* steps above,
  then run the bot inside a `screen`/`tmux`/`systemd` session so it stays
  alive 24/7.

## 🔑 Notes

- The assistant account (from `STRING_SESSION`) must be a **member of
  every group** where you want music to play, and voice chats must be
  started by a human/admin before `/play` will work.
- Add the bot to a group as **admin** so it can manage voice chats.
- To scale to many concurrent groups, you can run multiple assistant
  accounts and load-balance chats between them — this starter uses a
  single assistant for simplicity.

---
Built following the feature set discussed for **Vani X Music**-style bots.
