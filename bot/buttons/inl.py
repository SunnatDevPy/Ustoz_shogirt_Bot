from aiogram import Bot
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def language_inl():
    ikb = InlineKeyboardBuilder()
    ikb.add(*[InlineKeyboardButton(text='🇺🇿Uz', callback_data='lang_uz'),
              InlineKeyboardButton(text='🇷🇺Ru', callback_data='lang_ru')])
    ikb.adjust(2)
    return ikb.as_markup()


def confirm_inl():
    ikb = InlineKeyboardBuilder()
    ikb.add(*[InlineKeyboardButton(text='✅Tasdiqlash✅', callback_data='confirm_form'),
              InlineKeyboardButton(text=_('❌Toxtatish❌'), callback_data='cancel_form')])
    ikb.adjust(2)
    return ikb.as_markup()


async def make_channels(channel_ids, bot):
    ikb = InlineKeyboardBuilder()
    for channel_id in channel_ids:
        data = await bot.create_chat_invite_link(chat_id=channel_id)
        ikb.row(InlineKeyboardButton(text=f'Kanal {channel_ids[channel_id]["title"]}', url=data.invite_link))
    ikb.row(InlineKeyboardButton(text=_('Tasdiqlash'), callback_data='confirm_channel'))
    return ikb.as_markup()


def confirm_channels(title, url):
    ikb = InlineKeyboardBuilder()
    ikb.add(*[InlineKeyboardButton(text=_("Kanal") + f'{title}', url=f'https://t.me/{url}')])
    ikb.add(*[InlineKeyboardButton(text="✅", callback_data='confirm_add_channel'),
              InlineKeyboardButton(text="❌", callback_data='cancel_add_channel')])
    ikb.adjust(1, 2)
    return ikb.as_markup()


async def show_channels(channels, bot: Bot):
    ikb = InlineKeyboardBuilder()
    for i in channels:
        channel = channels[i]
        data = await bot.create_chat_invite_link(int(i))
        ikb.add(*[InlineKeyboardButton(text=channel['title'], callback_data='channel_name'),
                  InlineKeyboardButton(text=i, callback_data='channel_id'),
                  InlineKeyboardButton(text='O\'tish', url=data.invite_link),
                  InlineKeyboardButton(text='❌', callback_data=f'clear_channel_{i}')])
    ikb.adjust(4, repeat=True)
    return ikb.as_markup()
