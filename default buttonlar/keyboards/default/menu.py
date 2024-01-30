from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Aiogram darslar'),
            KeyboardButton(text='Boshqa foydali videolar'),
        ],
    ],
    resize_keyboard=True
)