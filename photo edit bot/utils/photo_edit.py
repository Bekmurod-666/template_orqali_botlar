from io import BytesIO
import aiohttp
from aiogram import types

from loader import bot

async def photo_link(poto: types.photo_size.PhotoSize) -> str:
    with await poto.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file
        )
        async with bot.session.post("https://telegra.ph/upload",data=form) as response:
            img_src = await response.json()
            print(img_src)
    link = "https://telegra.ph/" + img_src[0]['src']
    return link