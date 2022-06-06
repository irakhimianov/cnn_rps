from aiogram import types
# from keyboards.inline import
from loader import dp, bot
from util import *


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def user_image(message: types.Message):
    await bot.send_message(text='получена картинка',
                           chat_id=message.from_user.id)