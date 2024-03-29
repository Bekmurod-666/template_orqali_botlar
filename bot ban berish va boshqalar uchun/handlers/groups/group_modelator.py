import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup,AdminFilter
from loader import dp


# /ro yoki !ro (read-only) kommandalri uchun handler
# foydalanuvchini read-only ya'ni faqat o'qish rejimida o'tkazib qo'yma
@dp.message_handler(IsGroup(),Command('ro',prefixes='!/'),AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
        # 5 minut izohni cheklash
        # command = '!ro' time='5' comment =[]
        # 50 minut izohni cheklash


        #time = 20 # bu yerda bizlar 20 minut ularga yoza olmasligini teklaymiz
        #command='!ro' time = '50' comment=['reklama','uchun','ban']

        time = int(time)

        # Ban vaqtini hisoblaymiz(hozirgi vaqt + n minut

        until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

        try:
            await message.chat.restrict(user_id=member_id,can_send_messages=False,until_date=until_date)
            await message.reply_to_message.delete()
        except aiogram.utils.exceptions.BadRequest as err:
            await message.answer(f"Xatolik! {err.args}")
            return

        await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} daqiqa Yoza olmaysiz\n" f"Sabab:\n <b>{comment}</b>")

        service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi")
        # 5 sekund kutib o'chirib tashaydi
        await asyncio.sleep(5)
        await message.delete()
        await service_message.delete()



#read-only qayta tiklaymiz
@dp.message_handler(IsGroup(),Command("unro",prefixes='!/'))
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    # service_message = await message.reply("Xabaringiz 5 sekundan so'ng o'chib ketadi")

    await asyncio.sleep(5)
    await message.chat.restrict(user_id=member_id,permissions=user_allowed,until_date=0)
    await message.reply(f"Foydalanuvchi {member.username} accountingiz tiklandi")

    # bu yerda yozgan xabrni o'chirib tashaydi
    # xabarni o'chirish
    # await message.delete()
    # await service_message.delete()

#Foydalanuvchini banga yuborish (guruhdan haydash)
@dp.message_handler(IsGroup(),Command('ban',prefixes='!/'))
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    meber_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=meber_id)

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.username} Guruhdan haydaldi")
    service_message = await message.reply("Xabaringiz 5 sekundan so'ng o'chib ketadi")

    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()



#Foydalanuvchini bandan chiqarish Foydalanuvchini guruhga qo'sha olmaymiz (o'zi qo'shilishi mumkin
@dp.message_handler(IsGroup(),Command('unban',prefixes='!/'))
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    meber_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=meber_id)

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.username} Ban dan chiqdi")
    service_message = await message.reply("Xabaringiz 5 sekundan so'ng o'chib ketadi")

    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()

