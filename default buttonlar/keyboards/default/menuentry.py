from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuEntry = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="0Kirish"),
        KeyboardButton(text="dars1"),
    ],
    [
        KeyboardButton(text="dars2"),
        KeyboardButton(text="dars3"),
    ],

    [
        KeyboardButton(text="dars4"),
        KeyboardButton(text="dars5"),
    ],
    [
        KeyboardButton(text="Bosh menu")
    ]
 ],
resize_keyboard=True
)