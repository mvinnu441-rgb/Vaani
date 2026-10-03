import os
import asyncio
import yt_dlp

from config import DOWNLOADS_DIR


def _human_duration(seconds: int) -> str:
    if not seconds:
        return "Live"
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


async def search_and_download(query: str, video: bool = False) -> dict:
    """
    Searches YouTube for `query` and downloads best audio (or video)
    stream. Returns a dict with title, duration, file_path, webpage_url.
    Runs the blocking yt-dlp call in a thread to avoid blocking the event loop.
    """

    def _run():
        ydl_opts = {
            "format": "best[height<=?720]" if video else "bestaudio/best",
            "outtmpl": os.path.join(DOWNLOADS_DIR, "%(id)s.%(ext)s"),
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "default_search": "ytsearch",
            "geo_bypass": True,
            "postprocessors": (
                []
                if video
                else [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ]
            ),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=True)
            if "entries" in info:
                info = info["entries"][0]
            file_path = ydl.prepare_filename(info)
            if not video:
                file_path = os.path.splitext(file_path)[0] + ".mp3"
            return {
                "title": info.get("title", "Unknown"),
                "duration": _human_duration(info.get("duration", 0)),
                "file_path": file_path,
                "webpage_url": info.get("webpage_url", ""),
                "is_video": video,
            }

    return await asyncio.to_thread(_run)
