#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 8186557))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7665348559:AAH2UQebDxbU1C9GR1-QZaixfsglcHf1k5s")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Anubarlo:Anubarlo@cluster0.ioiefbq.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID","-1002718737593"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6848908141"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/abbasghazal/music2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

CH_US = getenv("CH_US", "lggbg")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/lggbg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/lggbg")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

SET_CMDS = getenv("SET_CMDS", "False")
# Get your pyrogram v2 session from @T66bot on Telegram
STRING1 = getenv("STRING_SESSION", "AgE-_xcAlgn9oQ8IAN99SJBnzrGd8DjgU2jF0PzcktZjhPGNb7sLJ_8OruDy9jUVmM9Yd75DXIiZSUzXuZg8r2OAKGxEUhmhnuVeaeDecNkWXcVyoSvEKFOmff4MxcsVmBR97aJqgw2rKWX7x6qc09TTLcibRNSAzxR3yiH7GfoNK0cIhoXUFda5-pgGV3yqvLs1VQHN87WnKoQYnE15HpTzsQq7ql3j7otPPa7mT5pijTzmIW4aXeU19q3J8bzWaxiFKiPC3Dd-IMcVYDj1OBmP1HqmvJp0Gg8jrR9xrrGm24kAMPcN-jDYpLHqReuwmJxJ2ekl7hN13dctL2e1F3vSyn7PZgAAAAHSXzHZAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
STATS_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
STREAM_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
