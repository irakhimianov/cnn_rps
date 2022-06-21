from aiogram import types
from keyboards.inline import retry_keyboard
from loader import dp, bot


@dp.callback_query_handler(text_contains="btn_retry")
async def image_create(call: types.CallbackQuery):
    await bot.send_message(text=f'Отправьте мне фото еще раз\n'
                                f'✊ ✌️ ✋',
                           chat_id=call.message.chat.id)
    await bot.answer_callback_query(call.id)