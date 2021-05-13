from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from callsmusic import *

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("durdur") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'duraklatıldı'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 Hiçbirşey oynamıyor!")
    else:
        callsmusic.pytgcalls.durdur_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🤐 duraklatıldı!")


@Client.on_message(command("devam") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'devam ettirildi'
    ):
        await message.reply_text(f"**{BN} :-** 🙄 Hiçbirşey duraklatılmadı!")
    else:
        callsmusic.pytgcalls.devam_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🥳 devam ettirildi!")


@Client.on_message(command("dur") & other_filters)
@errors
@authorized_users_only
async def dur(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** 🙄 Hiçbir şey çalışmıyor!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**{BN} :-** ❌ Akışı durdurdu!")


@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** 🙄 Atlamak için hiçbir şey oynamıyor!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text(f"**{BN} :-** 😬 Geçerli şarkıyı atladı!")
