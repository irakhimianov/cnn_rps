from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
# from keyboards.inline import
from loader import dp, bot
from util import *


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await bot.send_message(text='hi', chat_id=message.from_user.id)