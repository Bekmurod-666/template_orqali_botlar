from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from aiogram.utils.markdown import hbold,hcode,hitalic,hunderline,hstrikethrough
from loader import dp

#html formatlash

@dp.message_handler(commands='info_html')
async def get_html(message: types.Message):
    # text = f"Assalomu aleykum {message.from_user.full_name}!\n"
    text = "Bu <b>qalin</b> shrift\n"
    text += "Bu <i>og'ma</i> shrift\n"
    text += "Bu <u>pastgi chiziq</u> shrift\n"
    text += "Bu <s>o'rtadagi chiziq</s> shrift\n"
    text += "Bu <a href='https://kun.uz'>kun uz sahifasi</a>\n"
    text += "Bu <code>print('salom')</code>\n"

    await message.answer(text)

#markdown formatlash
@dp.message_handler(commands='info_markdown')
async def get_mark(message: types.Message):
    # text = f"Assalomu aleykum {message.from_user.full_name}!\n"
    text = "Bu *Qalin shrift markdown usulida* shrift\n"
    text += "~o'rtadan chiziq~\n"
    text += f"[kun uz sahifasi](https://kun.uz)"


    await message.answer(text,parse_mode=types.ParseMode.MARKDOWN_V2)




@dp.message_handler(commands='info_aiogram')
async def bot_help(message: types.Message):
    # text = f"Assalomu aleykum {message.from_user.full_name}!\n"
    text = "Bu " + hbold('qalin \n')
    text += "Bu " + hitalic('ogma \n')
    text += "Bu " + hunderline('pastki chiziq \n')
    text += "Bu " + hstrikethrough('orta chiziq \n')
    text += "Bu " + hcode('@dp.message_handler(commands="info_aiogram")\n')

    await message.answer(text)