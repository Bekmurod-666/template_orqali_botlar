from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Command
from aiogram.utils.markdown import hbold,hitalic,hlink,hcode,hunderline,hstrikethrough
from loader import dp

#html formatlash

@dp.message_handler(Command('info_html'))
async def get_html(msg: types.Message):
    text = f"Assalomu aleykum {msg.from_user.full_name}!\n"
    text += "Bu <b>Qalin</b> shrift\n"
    text += "Bu <i>Og'ma</i> shrift\n"
    text += "Bu <u>pastki chiziq</u> shrift\n"
    text += "Bu <s>O'rtadagi chiziq</s> shrift\n"
    text += "Bu <a href='https://kun.uz'>Kun uz sahifasi</a>\n"
    text += "Bu <code>print('salom')</code>/n"

    await msg.answer(text)


#markdown formatlash
@dp.message_handler(Command('info_markdown'))
async def get_markdown(msg: types.Message):
    text = f"Assalomu aleykum {msg.from_user.full_name}!\n"
    text += "Bu *Qalin shrift markdown usulida* shrift\n"
    text += "Bu ~O'rtadan chiziq~\n"
    text += "[Kun uz sahifasi](https://kun.uz)"

    await msg.answer(text,parse_mode=types.ParseMode.MARKDOWN_V2)


@dp.message_handler(Command('info_aiogram'))
async def get_aiogram(msg: types.Message):
    text = f"Assalomu aleykum {msg.from_user.full_name}!\n"
    text += "Bu " + hbold("Qalin\n")
    text += "Bu " + hitalic("og'ma\n")
    text += "Bu " + hunderline("Pastki chiziq\n")
    text += "Bu " + hstrikethrough("O'rta chiziq\n")
    text += "Bu " + hcode("@dp.message_handler(Command('info_aiogram'))\n")

    await msg.answer(text)



