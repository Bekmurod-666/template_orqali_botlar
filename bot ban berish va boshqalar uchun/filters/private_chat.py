from aiogram import types

from aiogram.dispatcher.filters import BoundFilter

class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type==types.ChatType.PRIVATE # manashu qo'd bizga shaxsiz chatdan yozilganmi yo'qligini aniqlab beradi
