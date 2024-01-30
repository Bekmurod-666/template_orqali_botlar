from aiogram.types import Message,CallbackQuery,ReplyKeyboardRemove

from keyboards.default.location_button import Keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp



@dp.callback_query_handler(text='mylocation')
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Locatsiya yuboring:",reply_markup=Keyboard)


@dp.message_handler(content_types='location')
async def get_contact(msg: Message):
    location = msg.location
    latitude = location.latitude
    longitude = location.longitude
    closest_hospital = choose_shortest(location)
    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Masofa: {distance:.1f} km."
                        for shop_name, distance, url, shop_location in closest_hospital])

    await msg.answer(f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_hospital:
        await msg.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
