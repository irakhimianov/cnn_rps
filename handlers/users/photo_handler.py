from aiogram import types
# from keyboards.inline import
from loader import dp, bot
from util import get_result
from models import RPS, RPS_EMOJI
from cnn import get_prediction


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def user_photo(message: types.Message):
    my_result = await send_game_result()
    await message.photo[-1].download(destination_file='static/temp.jpg')
    await bot.send_message(text=f'получена картинка:\n'
                                f'результат бота: {my_result[0]} {my_result[1]}',
                           chat_id=message.from_user.id)
    predict = get_prediction('static/temp.jpg')
    await bot.send_message(text=f'получен ответ\n'
                                f'результат: {predict}',
                           chat_id=message.from_user.id)

async def send_game_result():
    bot_result = get_result()
    return bot_result