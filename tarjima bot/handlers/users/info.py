from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Command

from loader import dp


@dp.message_handler(Command('info'))
async def bot_info(message: types.Message):
    await message.answer("Bu bot aiogram tomonidan mahsus yaratilgan")
