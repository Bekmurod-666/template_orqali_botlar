from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id) # bu yerda yozgan odamni id nini olib o'zgaruvchiga tenglashtiradi
        return member.is_chat_admin()