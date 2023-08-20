## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAFCQJwAcjfNoeNgP1F-KhXg8nRMfpaZlnlQ30QHebqtqglirTo3tkDJZ9NU-NfC8VyIsV0s1oLnE783IYody60ElsfGS211DjsYBV36jQGMaBliu6rG6oCrSVLpsfowmS8sipi5Ryy")
BOT_TOKEN = getenv("BOT_TOKEN", "5889085407:AAHSyJtD6xPwGGktbE5nnwXpOqB4Fjq3HW8")
BOT_NAME = getenv("BOT_NAME", "Mamaklı Music")
API_ID = int(getenv("API_ID", 21119132))
API_HASH = getenv("API_HASH", "c0a90d0ba66e6bdea356894a55f4856e")
OWNER_NAME = getenv("OWNER_NAME", "Mamaklı")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "mamaklimusic")
BOT_USERNAME = getenv("BOT_USERNAME", "vefamusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Mamaklı Müzik")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "mamaklimekani")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mamaklibirininruhu")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5905988205").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/memomuzik/RaiChuMusic")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
