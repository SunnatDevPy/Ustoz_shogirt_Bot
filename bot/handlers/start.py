from aiogram import Router, Bot, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from redis_dict import RedisDict

from bot.buttons.inl import language_inl
from bot.buttons.simple import menu_btn
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.detail.detail_text import start_text

start_router = Router()
users_db = RedisDict('users')


@start_router.message(CommandStart())
async def handler_start(message: Message, bot: Bot):
    await message.answer(_('Til tanlang'), reply_markup=language_inl())
    await message.answer(text=start_text(message), reply_markup=menu_btn(), parse_mode=ParseMode.MARKDOWN)


@start_router.message(Command('help'))
async def handler_start(message: Message, bot: Bot):
    text = ''''
UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. 

Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 

E'lon berish: @UstozShogirdBot

Admin @UstozShogirdAdminBot')'''
    await message.answer(text)
