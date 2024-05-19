from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

def send_contact_btn():
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text=_('📞Contact jo\'natish📞'), request_contact=True))
    return kb.as_markup(resize_keyboard=True)


def menu_btn():
    kb = ReplyKeyboardBuilder()
    kb.add(*[KeyboardButton(text=_('Sherik kerak')),
             KeyboardButton(text=_('Ish joyi kerak')),
             KeyboardButton(text=_('Hodim kerak')),
             KeyboardButton(text=_('Ustoz kerak')),
             KeyboardButton(text=_('Shogirt kerak'))])
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True)
