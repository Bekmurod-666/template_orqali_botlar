from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

otherbutton = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text="aiogram darslar"),
        KeyboardButton(text="👉Ikkinchi tugma"),
    ],
],
    resize_keyboard=True
)