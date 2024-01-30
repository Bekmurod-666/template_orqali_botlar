from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.default.menuentry import menuEntry
from keyboards.default.otherButton import otherbutton

from keyboards.default.menu import menu

from loader import dp

@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Tugmalarni bosing',reply_markup=menu)

@dp.message_handler(text='Aiogram darslar')
async def show_menu(message: Message):
    await message.answer('Darslarni tanlang',reply_markup=menuEntry)

@dp.message_handler(text='Boshqa foydali videolar')
async def show_menu(message: Message):
    await message.answer('Tugmalarni bosing',reply_markup=otherbutton)

