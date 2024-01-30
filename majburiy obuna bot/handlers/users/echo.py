from aiogram import types

from loader import dp
import wikipedia

wikipedia.set_lang('uz')


@dp.message_handler()
async def check_wiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday malumot yo'q")
