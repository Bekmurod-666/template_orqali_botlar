from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp,db


@dp.message_handler(Command("email"))
async def bot_start(msg: types.Message,state: FSMContext):
    await msg.answer("Emailingizni yuboring")
    await state.set_state('email')


@dp.message_handler(state='email')
async def enert_email(msg: types.Message,state: FSMContext):
    email = msg.text
    db.update_user_email(email = email,id = msg.from_user.id)
    user = db.select_user(msg.from_user.id)
    await msg.answer(f"Baza yangilandi: {user}")
    await state.finish()




