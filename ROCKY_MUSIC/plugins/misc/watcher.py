from pyrogram import filters
from pyrogram.types import Message

from ROCKY_MUSIC import app
from ROCKY_MUSIC.core.call import ROCKY

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await ROCKY.stop_stream_force(message.chat.id)
