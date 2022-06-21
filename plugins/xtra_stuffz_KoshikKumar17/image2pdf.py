# (c) @KoshikKumar17
import os
from PIL import Image
from pyrogram import Client,filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

LIST = {}

@Client.on_message(filters.private & filters.photo)
async def pdf(client,message):
 
 if not isinstance(LIST.get(message.from_user.id), list):
   LIST[message.from_user.id] = []

  
 
 file_id = str(message.photo.file_id)
 ms = await message.reply_text("Converting to PDF ......")
 file = await client.download_media(file_id)
 
 image = Image.open(file)
 img = image.convert('RGB')
 LIST[message.from_user.id].append(img)
 await ms.edit(f"{len(LIST[message.from_user.id])} image **Successfully created PDF**. If you want to add more image, Send me **One by One**\n\n If done **click** here 👉 __/c2pdf__")
 

@Client.on_message(filters.command(['c2pdf']))
async def done(client,message):
 images = LIST.get(message.from_user.id)

 if isinstance(images, list):
  del LIST[message.from_user.id]
 if not images:
  await message.reply_text( "No image !!🤷🏻🤷🏻")
  return

 path = f"{message.from_user.id}@KoshikKumar17.pdf"
 images[0].save(path, save_all = True, append_images = images[1:])

 await client.send_document(message.from_user.id, open(path, "rb"), caption = "Heya!! Here your PDF !!")
 os.remove(path)
