import io
from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp,bot


@dp.message_handler(IsGroup(),Command("change_photo",prefixes="!/"))
async def set_photo(message: types.Message):
    s_message = message.reply_to_message
    photo = s_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    await message.chat.set_photo(photo=input_file)
