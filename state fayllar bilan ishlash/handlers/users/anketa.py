from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData


@dp.message_handler(Command('anketa'),state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ismizngizni kiriting")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message,state: FSMContext):
    fullname = message.text

    await state.update_data({'name': fullname})

    await message.answer("Emailingizni kiriting")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message,state:FSMContext):
    email = message.text

    await state.update_data({'email': email})

    await message.answer("Telefon raqamni kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNume)
async def answer_phoneNum(message: types.Message,state: FSMContext):
    phone = message.text

    await state.update_data({'phone': phone})

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Quydagilar malumotlarni qabul qilindi: \n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Emailingiz - {email}\n"
    msg += f"Telefon raqam - {phone}"

    await message.answer(msg)
    await state.finish()
