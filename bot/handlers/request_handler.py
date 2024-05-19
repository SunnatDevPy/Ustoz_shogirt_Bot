from aiogram import Router, F, Bot
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from bot.buttons.inl import confirm_inl
from bot.buttons.simple import send_contact_btn, menu_btn
from bot.detail.detail_form_text import detail_form
from bot.detail.detail_text import name_detail, technology_detail, contact_detail, area_detail, \
    price_detail, age_detail, appeal_detail, detail_goal, start_detail_keyboard, detail_job
from config.conf import BOT_CONFIG
from states.state import FormState

request_router = Router()

import re


def check_phone(phone: str):
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{11,14}$"
    check = re.findall(validate_phone_number_pattern, phone)
    return check


@request_router.message(
    F.text.in_([__('Sherik kerak'), __('Ish joyi kerak'), __('Hodim kerak'), __('Ustoz kerak'), __('Shogirt kerak')]))
async def request_start(message: Message, state: FSMContext):
    button = message.text.split(_('kerak'))[0].strip()
    await state.set_state(FormState.name)
    await state.update_data(button=button)
    await message.answer(start_detail_keyboard(button), parse_mode=ParseMode.MARKDOWN)
    if button == _('Hodim'):
        await message.answer(_('🎓 Idora nomi?'), parse_mode=ParseMode.MARKDOWN)
        return
    await message.answer(name_detail(), parse_mode=ParseMode.MARKDOWN)


@request_router.message(FormState.name)
async def request_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await state.set_state(FormState.age)
    if data['button'] == _('Hodim'):
        await message.answer(_('✍️Mas\'ul ism sharifi?'), parse_mode=ParseMode.MARKDOWN)
        return
    await message.answer(age_detail(), parse_mode=ParseMode.MARKDOWN)


@request_router.message(FormState.age)
async def request_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(FormState.technology)
    await message.answer(technology_detail(), parse_mode=ParseMode.MARKDOWN)


@request_router.message(FormState.technology)
async def request_technology(message: Message, state: FSMContext):
    await state.update_data(technology=message.text)
    await state.set_state(FormState.contact)
    await message.answer(contact_detail(), reply_markup=send_contact_btn(), parse_mode=ParseMode.MARKDOWN)


@request_router.message(FormState.contact)
async def request_contact(message: Message, state: FSMContext):
    if message.contact:
        await state.update_data(contact=message.contact.phone_number)
        await state.set_state(FormState.area)
        await message.answer(area_detail(), parse_mode=ParseMode.MARKDOWN, reply_markup=None)
    elif message.text and check_phone(message.text):
        await state.update_data(contact=message.text)
        await state.set_state(FormState.area)
        await message.answer(area_detail(), parse_mode=ParseMode.MARKDOWN, reply_markup=None)
    else:
        await message.answer(_('Yuborgan malumot telefon raqam emas'))



@request_router.message(FormState.area)
async def request_area(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(area=message.text)
    await state.set_state(FormState.price)
    if data['button'] == __('Hodim'):
        await message.answer(_('💰 Maoshni kiriting?'), parse_mode=ParseMode.MARKDOWN)
        return
    await message.answer(price_detail(), parse_mode=ParseMode.MARKDOWN)


@request_router.message(FormState.price)
async def request_price(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(price=message.text)
    await state.set_state(FormState.job)
    if data['button'] == __('Hodim'):
        await message.answer(_("🕰 Ish vaqtini kiriting?"), parse_mode=ParseMode.MARKDOWN)
        return
    await message.answer(detail_job(), parse_mode=ParseMode.MARKDOWN)


@request_router.message(FormState.job)
async def request_price(message: Message, state: FSMContext):
    await state.update_data(job=message.text)
    await state.set_state(FormState.appeal)
    await message.answer(appeal_detail(), parse_mode=ParseMode.MARKDOWN)


@request_router.message(FormState.appeal)
async def request_appeal(message: Message, state: FSMContext):
    await state.update_data(appeal=message.text)
    await state.set_state(FormState.goal)
    await message.answer(detail_goal(), parse_mode=ParseMode.MARKDOWN)



@request_router.message(FormState.goal)
async def request_goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    await state.set_state(FormState.about)
    data = await state.get_data()
    if data['button'] == __('Hodim'):
        await message.answer(_("‼️ Qo`shimcha ma`lumotlar?"), parse_mode=ParseMode.MARKDOWN)
        return


@request_router.message(FormState.about)
async def request_confirm(message: Message, state: FSMContext):
    await state.update_data(about=message.text)
    data = await state.get_data()
    await message.answer(detail_form(message, data), reply_markup=confirm_inl(), parse_mode=ParseMode.MARKDOWN)


@request_router.callback_query(F.data.in_(['confirm_form', 'cancel_form']))
async def request_cancel_form(call: CallbackQuery, state: FSMContext, bot:Bot):
    data = await state.get_data()
    if call.data == 'confirm_form':
        await bot.send_message(chat_id=BOT_CONFIG.ADMIN_ID, text=detail_form(call, data), parse_mode=ParseMode.MARKDOWN, reply_markup=menu_btn())
        await call.message.answer(_('Adminga jo\'natildi'), reply_markup=menu_btn())
    elif call.data == 'cancel_form':
        await call.message.answer(_('Protsess toxtatildi'))
    await call.message.delete()
    await state.clear()
