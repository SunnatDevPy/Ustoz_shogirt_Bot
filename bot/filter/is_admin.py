from aiogram.filters import Filter
from aiogram.types import Message


class IsAdmin(Filter):
    def __init__(self, admin_list: list | tuple | int) -> None:
        self.admin_list = admin_list

    async def __call__(self, message: Message) -> bool:
        if self.admin_list == int:
            return message.from_user.id == self.admin_list
        return message.from_user.id in self.admin_list