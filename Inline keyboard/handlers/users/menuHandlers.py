from aiogram.types import Message,CallbackQuery

from keyboards.inline.mahsulotKeyboard import categoryMenu,course_callback,coursesMenu
from loader import dp
import logging

@dp.message_handler(text_contains = 'Mahsulot')
async def get_category(message: Message):
    await message.answer("Mahsulotni tanlang",reply_markup=categoryMenu)


@dp.callback_query_handler(text='courses')
async def by_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    logging.info(f"{call.from_user.id=}")
    logging.info(f"{call.from_user.full_name=}")
    await call.message.answer("Kurs tanlang",reply_markup=coursesMenu)
    await call.answer(cache_time=60)