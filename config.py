import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/d83a7508f61b911bea669.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO" , "https://github.com/dev-logesh/tgmusicbot")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/e2b3993f803f5166c277d.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/8bd4ebad3985224bb48b8.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/2d8eed4477e6650e3b260.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/0d743d6576089fe61a4bf.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
