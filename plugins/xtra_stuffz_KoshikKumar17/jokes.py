# (c) @KoshikKumar17
import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://v2.jokeapi.dev/joke/Any?type="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🙋‍♂️Father🙋‍♂️', url='https://t.me/KoshikKumar17')]])

@Client.on_message(filters.command("joke"))
async def reply_info(bot, update):
    koshik = await update.reply_text("Getting a Joke...😂")
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await koshik.edit_text(
        text=gett_joke(query),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def gett_joke(type):
    try:
        r = requests.get(API + requote_uri(type.lower()))
        info = r.json()
        joke = info['joke']
        return f"""
😁Here is Your Joke😁 :\n \n **{joke}**
\nWith ❤️ by @KoshikKumar17"""

    except Exception as error:
        return error
