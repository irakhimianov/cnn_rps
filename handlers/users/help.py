from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp(), state=None)
async def cmd_help(message: types.Message):
    message_text = f"Привет!\n"\
                   f"Игра в камень-ножницы-бумага!"
    await message.answer(text=message_text)