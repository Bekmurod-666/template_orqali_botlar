import types

from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.default.menuentry import menuEntry

from keyboards.default.menu import menu

from loader import dp

@dp.message_handler(text='0Kirish')
async def video0(message: Message):
    await message.answer("https://www.youtube.com/watch?v=okxVdTqx3ak&list=PLf9xy3Z3gtwkMbLdsooeqLzTujf_iI4b9")


@dp.message_handler(text='dars1')
async def video1(message: Message):
    await message.answer("https://www.youtube.com/watch?v=ovwA274sQzE&list=PLf9xy3Z3gtwkMbLdsooeqLzTujf_iI4b9&index=2")


@dp.message_handler(text='dars2')
async def video2(message: Message):
    await message.answer("https://www.youtube.com/watch?v=o5X6wTbsYGs&list=PLf9xy3Z3gtwkMbLdsooeqLzTujf_iI4b9&index=3")


@dp.message_handler(text='dars3')
async def video3(message: Message):
    await message.answer("https://www.youtube.com/watch?v=4ZedMr5AAk8&list=PLf9xy3Z3gtwkMbLdsooeqLzTujf_iI4b9&index=4")


@dp.message_handler(text='dars4')
async def video4(message: Message):
    await message.answer("https://www.youtube.com/watch?v=ehjGWfLixeU&list=PLf9xy3Z3gtwkMbLdsooeqLzTujf_iI4b9&index=5")


@dp.message_handler(text='dars5')
async def video5(message: Message):
    await message.answer("https://www.youtube.com/watch?v=t0hfLv3Y2D4&list=PLf9xy3Z3gtwkMbLdsooeqLzTujf_iI4b9&index=6")


@dp.message_handler(text="Bosh menu")
async def home(message: Message):
    await message.answer("Tugmalarni tanlang",reply_markup=menu)