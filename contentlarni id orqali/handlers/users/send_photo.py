from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import bot,dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def getfilephoto(msg: types.Message):
    await msg.reply(msg.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def getfile_video(msg: types.Message):
    await msg.reply(msg.video.file_id)


@dp.message_handler(Command('test'))
async def send_test(msg: types.Message):
    photo_id1 = "AgACAgIAAxkBAAIFo2Wa0mU1B4Yo8UHTwVUR6mk5TWANAALR2DEb7avZSCe4ahOC4scUAQADAgADeAADNAQ"
    photo_id2 = "AgACAgIAAxkBAAIFpWWa0mlq8TPIa0mCtsaqsO3Jstm1AAL-2DEb7avZSCJ-5x3vBelLAQADAgADeAADNAQ"
    photo_link = "https://www.uhdpaper.com/2023/11/sunset-mountain-retrowave-4k-1871n.html"
    photo_file = InputFile(path_or_bytesio="photos/supramk4.jpg")
    await msg.reply_photo(photo_id1,caption="Bu rasim1 id orqali yuborildi")
    await msg.reply_photo(photo_id2,caption='Bu rasim2 id oqali yuborildi')
    await msg.reply_photo(photo_link,caption="Bu rasim3 id orqali yuborildi")
    await bot.send_photo(chat_id=msg.from_user.id,photo= photo_file,caption="Bu rasim local xotiradan keldi")


@dp.message_handler(Command('album'))
async def send_album(msg: types.Message):
    await msg.answer('Biroz kuting...')
    album = types.MediaGroup()
    photo_id1 = "AgACAgIAAxkBAAIFo2Wa0mU1B4Yo8UHTwVUR6mk5TWANAALR2DEb7avZSCe4ahOC4scUAQADAgADeAADNAQ"
    photo_id2 = "AgACAgIAAxkBAAIFpWWa0mlq8TPIa0mCtsaqsO3Jstm1AAL-2DEb7avZSCJ-5x3vBelLAQADAgADeAADNAQ"
    photo_link = "https://www.uhdpaper.com/2023/11/sunset-mountain-retrowave-4k-1871n.html"
    photo_file = InputFile(path_or_bytesio="photos/supramk4.jpg")
    album.attach_photo(photo = photo_id1)
    album.attach_photo(photo=photo_id2)
    album.attach_photo(photo=photo_link)
    album.attach_photo(photo=photo_file)


    await msg.reply_media_group(media=album)