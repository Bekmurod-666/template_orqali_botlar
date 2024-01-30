from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .private_chat import IsPrivate
from .group_filter import IsGroup
from .admins import AdminFilter

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(AdminFilter)

