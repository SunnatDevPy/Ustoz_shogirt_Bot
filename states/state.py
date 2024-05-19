from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State


class FormState(StatesGroup):
    name = State()
    age = State()
    technology = State()
    contact = State()
    area = State()
    price = State()
    job = State()
    appeal = State()
    goal = State()
    about = State()
    confirm = State()


class AddChannelState(StatesGroup):
    chat_id = State()
    confirm = State()


class ForwardState(StatesGroup):
    chat_id = State()
