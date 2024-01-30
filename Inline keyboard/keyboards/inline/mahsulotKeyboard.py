from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.inline.callback_data import course_callback


categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻Kurslar",callback_data="courses"),
            InlineKeyboardButton(text="📗Kitoblar",callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="📽️Youtube sahifa",url="https://www.youtube.com/")
        ],
        [
            InlineKeyboardButton(text='🔍Qidirish',switch_inline_query="")
        ],
        [
            InlineKeyboardButton(text="⏩Ulashish",switch_inline_query="Foydali bot")
        ],
    ],

)

# 2-Usuli

coursesMenu = InlineKeyboardMarkup(row_width=1)
entry = InlineKeyboardButton(text="Entry Darslar",callback_data=course_callback.new(item_name='entry'))
coursesMenu.insert(entry)
python= InlineKeyboardButton(text="Python Darslar",callback_data=course_callback.new(item_name='python'))
coursesMenu.insert(python)