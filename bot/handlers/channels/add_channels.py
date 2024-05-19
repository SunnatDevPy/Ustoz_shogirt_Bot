from aiogram import Router, Bot, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from redis_dict import RedisDict

from bot.buttons.inl import confirm_channels, show_channels
from bot.detail.detail_text import channel_detail
from bot.filter.is_admin import IsAdmin
from config.conf import BOT_CONFIG
from states.state import ForwardState, AddChannelState

channels_db = RedisDict('channels_db')
bot_db = RedisDict('bot_db')

ADMINS = int(BOT_CONFIG.ADMIN_ID),
channels_router = Router()

''' ============       Get ID handler      =============='''


@channels_router.message(Command('get_id'), IsAdmin(ADMINS))
async def get_id(message: Message, state: FSMContext):
    await state.set_state(ForwardState.chat_id)
    await message.answer(text='Forward qilib message tashlang')


@channels_router.message(ForwardState.chat_id, IsAdmin(ADMINS))
async def get_id(message: Message, state: FSMContext):
    chat_id = ''
    username = ''
    type = 'private'
    if message.forward_from:
        chat_id = message.forward_from.id
        username = message.forward_from.username
        type = 'Bot' if message.forward_from.is_bot == True else 'User'
    if message.forward_from_chat:
        chat_id = message.forward_from_chat.id
        username = message.forward_from_chat.username
        type = message.forward_from_chat.type
    text = f'''
Forward {type}
chat_id: <code>{chat_id}</code>
Username: <code>@{username}</code>
    '''
    await message.answer(text=text, parse_mode='html')
    await state.clear()


'''============     CHANAL and BOTS add handler   ===================='''


@channels_router.message(Command('add'), IsAdmin(ADMINS))
async def add_channel(message: Message, state: FSMContext):
    await state.set_state(AddChannelState.chat_id)
    await message.answer('Chat id ni kiriting')


@channels_router.message(AddChannelState.chat_id, IsAdmin(ADMINS))
async def add_channel(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(AddChannelState.chat_id)
    chat = await bot.get_chat(message.text)
    if chat:
        await state.update_data(info_chat=chat)
        await state.set_state(AddChannelState.confirm)
        text = channel_detail(chat)
        await message.answer(text, parse_mode=ParseMode.MARKDOWN_V2,
                             reply_markup=confirm_channels(chat.title, chat.username))
    else:
        await message.answer('Chat id notog\'ri')


@channels_router.callback_query(AddChannelState.confirm, F.from_user.id.in_(ADMINS))
async def confirm_channel(call: CallbackQuery, state: FSMContext, bot:Bot) -> None:
    if call.data == 'confirm_add_channel':
        data = await state.get_data()
        channel = data['info_chat']
        try:
            channels_db[str(channel.id)] = (await bot.get_chat(channel.id)).model_dump_json()
        except TelegramBadRequest as e:
            await call.message.answer('Kanalda yo\'qmanku')
        await call.message.delete()
        await call.message.answer(f'Yangi {channel.type} qo\'shildi')
        await state.clear()
    elif call.data == 'cancel_add_channel':
        await call.message.delete()
        await call.message.answer('Protsess toxtatildi')
        await state.clear()


@channels_router.message(Command('channels'), IsAdmin(ADMINS))
async def list_channels(message: Message, bot:Bot):
    if channels_db:
        await message.answer('Kanallar ro\'yxati', reply_markup=await show_channels(channels=channels_db, bot=bot))
    else:
        await message.answer('Kanallar xali qoshilmagan')


@channels_router.callback_query(F.data.startswith('clear_channel'), F.from_user.id.in_(ADMINS))
async def clear_channel(call: CallbackQuery, bot:Bot):
    data = call.data.split('_')[-1]
    del channels_db[data]
    await call.answer(f'Kanal o\'chdi {data}', show_alert=True)
    await call.message.edit_text('Kanallar ro\'yxati', reply_markup=await show_channels(channels=channels_db, bot=bot))

