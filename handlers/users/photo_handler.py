from aiogram import types
# from keyboards.inline import
from loader import dp, bot
from util import get_result


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def user_photo(message: types.Message):
    await message.photo[-1].download(destination_file='static/temp.jpg')
    await bot.send_message(text='получена картинка',
                           chat_id=message.from_user.id)


async def send_game_result():
    bot_result = get_result()