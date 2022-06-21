from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


retry_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1)
btn_retry= InlineKeyboardButton(text="Сыграем еще раз? ♻️", callback_data="btn_retry")
retry_keyboard.add(btn_retry)