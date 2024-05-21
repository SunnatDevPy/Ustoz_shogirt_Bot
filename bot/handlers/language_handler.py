from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _

from bot.buttons.simple import menu_btn
from bot.detail.detail_text import start_text

language_router = Router()


@language_router.callback_query(F.data.startswith('lang_'))
async def language_handler(call: CallbackQuery, state: FSMContext):
    lang_code = call.data.split('lang_')[-1]
    await state.update_data(locale=lang_code)
    await call.answer(_(_('Til tanlandi' , locale=lang_code)), show_alert=True)
    await call.message.answer('/start ' , locale=lang_code)



'install i18n'
# pip install Babel
# pip install aiogram[i18n]
