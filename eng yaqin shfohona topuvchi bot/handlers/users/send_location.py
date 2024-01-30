from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from keyboards.inline.location_button import location_keys
from loader import dp,bot

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_photo(msg: types.Message):
    await msg.reply(msg.photo[-1].file_id)

@dp.message_handler(Command('shifohona'))
async def send_kommand(msg: types.Message):
    photo_id = "AgACAgIAAxkBAAIF6GWeZ6_VW4_3bU2VzlzhR010vkogAAIm2zEbxWDxSIZ5u9PSE_V9AQADAgADbQADNAQ"
    rasim_about = "<b>shifoxona</b>"
    await msg.reply_photo(photo_id, caption=rasim_about, reply_markup=location_keys)
