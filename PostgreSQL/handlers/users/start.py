import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS

from loader import dp,db,bot


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    try:
        user = await db.add_user(telegram_id=msg.from_user.id,
                                 full_name=msg.from_user.full_name,
                                 username=msg.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telgram_id = msg.from_user.id)

    await msg.answer("Xush kelibsiz")

    #Adminga xabar yuboramiz
    cont = await db.count_users()
    xabar = f"{user[1]} bzaga qo'shildi.\nBazada {cont} ta foydalanuvchi bor"
    await bot.send_message(chat_id=ADMINS[0],text=xabar)
