from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .admins import AdminFilter
from .group_filter import IsGroup
from .private_chat import IsPrivate


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)

