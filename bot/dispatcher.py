from aiogram import Bot, Dispatcher

from config.conf import BOT_CONFIG

bot = Bot(token=BOT_CONFIG.BOT_TOKEN)
dp = Dispatcher()