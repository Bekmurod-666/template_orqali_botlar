import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp,db,bot


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    name = msg.from_user.first_name
    #Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id = msg.from_user.id,name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0],text=err)

    await msg.answer("Xush kelibsiz!")
    #Admin ga Xabar beramiz
    count = db.count_users()[0]
    mssg = f"{msg.from_user.first_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor"
    await bot.send_message(chat_id=ADMINS[0],text=mssg)
