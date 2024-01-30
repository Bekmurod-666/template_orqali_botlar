from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
Keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text='Locatsiya yuborish', request_location=True)
                                   ]
                               ])
