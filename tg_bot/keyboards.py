from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


initial_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Русский язык', callback_data='rus')],
    [InlineKeyboardButton(text='Кубачинский язык', callback_data='kubach')]
])