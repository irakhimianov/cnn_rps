from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await bot.send_message(text=f'Выпускная квалификационная работа\n'
                                f'Программная реализация сверточных нейронных сетей для распознавания изображений.\n\n'
                                f'Отправьте фото для игры в камень-ножницы-бумага',
                           chat_id=message.from_user.id)