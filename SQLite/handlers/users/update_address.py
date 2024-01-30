from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from utils.db_api.sqlite import

from loader import dp,db

@dp.message_handler(Command("address"))
async def bot_start(msg: types.Message,state: FSMContext):
    await msg.answer("Addressingizni yubring")
    await state.set_state('address')


@dp.message_handler(state='address')
async def enert_address(msg: types.Message,state: FSMContext):
    address = msg.text
    db.enter_address(address = address,id = msg.from_user.id)
    user = db.select_user(msg.from_user.id)
    await msg.answer(f"Baza yangilandi: {user}")
    await state.finish()