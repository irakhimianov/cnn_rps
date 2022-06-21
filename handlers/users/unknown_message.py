from aiogram import types
from loader import dp, bot


@dp.message_handler()
async def unknown_message(message: types.Message):
    await bot.send_message(text=f'Извините, я не понял Ваш запрос.\n'
                                f'Отправьте команду /start',
                           chat_id=message.from_user.id)