import asyncio
import logging
import sys

from aiogram import Bot, F
from aiogram.types import BotCommandScopeChat, BotCommand, CallbackQuery
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from bot.dispatcher import bot, dp
from bot.handlers.channels.add_channels import channels_router
from bot.handlers.language_handler import language_router
from bot.handlers.request_handler import request_router
from bot.handlers.start import start_router
from bot.middleware.mandatory_channel import JoinChannelMiddleware
from config.conf import BOT_CONFIG


async def on_start(bot: Bot):
    commands = [
        BotCommand(command='start', description="Bo'tni ishga tushirish"),
        BotCommand(command='help', description="Yordam"),
        BotCommand(command='add', description="Kanal qoshish"),
        BotCommand(command='channels', description="Kanallar royxati"),
        BotCommand(command='bots', description="botlar"),
        BotCommand(command='get_id', description="id qaytarish")

    ]
    s = BotCommandScopeChat(chat_id=BOT_CONFIG.ADMIN_ID)
    await bot.set_my_commands(commands=commands, scope=s)


async def main():
    dp.startup.register(on_start)
    dp.include_routers(request_router, start_router, language_router, channels_router)
    i18n = I18n(path="locales", default_locale='uz')
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    # dp.update.outer_middleware(JoinChannelMiddleware())
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
