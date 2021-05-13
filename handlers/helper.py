from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("help") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""💞 Hello! Following are the commands available for **{bn}** - __A Group Voice Chat Music Player__.
The commands I currently support are:

🔥 **Users Commands :**
⚜️ /oynat - **[ Groups Only ]** > __Plays the replied audio file or YouTube video through link.__
⚜️ /song - **[ Groups & DM ]** > __Uploads the searched song in the chat.__
⚜️ /ytplay - **[ Groups Only ]** > __Plays the song directly from YouTube Search.__
⚜️ /repo - **[ DM Only ]** > __Gets the source code and YouTube Tutorial Video.__


🔰 **Admin & Sudo Users Commands :**
⚜️ /durdur - **[Groups Only ]** > __Pause Voice Chat Music.__
⚜️ /devam - **[Groups Only ]** > __Resume Voice Chat Music.__
⚜️ /atla - **[Groups Only ]** > __Skips the current Music Playing In Voice Chat.__
⚜️ /dur - **[Groups Only ]** > __Clears The Queue as well as ends Voice Chat Music.__""")

@Client.on_message(command("yardım") & other_filters)
async def gyardım(_, message: Message):
    await message.reply_text(f"**{bn} :-** selam! Tüm komutları almak için beni PM bakınız 😉")
