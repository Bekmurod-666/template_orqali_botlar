from aiogram import types
from aiogram.dispatcher.filters import CommandStart,Command

from loader import dp

@dp.message_handler(Command('info'))
async def info_handler(msg: types.Message):
    await msg.answer("Bu bot aiogram tomonidan maxsus yaratilgan")