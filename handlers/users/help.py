from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp(), state=None)
async def cmd_help(message: types.Message):
    message_text=f"Бот для демонстрации работы разработанной модели <b>сверточной нейронной сети</b>\n" \
                 f"Автор: <b>Рахимьянов Ильгиз</b> @rkjar"
    await message.answer(text=message_text)