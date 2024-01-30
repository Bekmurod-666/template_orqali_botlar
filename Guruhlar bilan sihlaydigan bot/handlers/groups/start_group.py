from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup
from loader import dp



@dp.message_handler(IsGroup(),CommandStart())
async def bots_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.username} Guruhga qo'shildingiz!")
