import logging
import asyncio
import keyboards

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

# Установка логгирования
logging.basicConfig(level=logging.INFO)

# Токен вашего бота (полученный от @BotFather)
BOT_TOKEN = '7492375983:AAGoT9haeErQmjjawuFNsKULWoJVJuU9ad4'

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.reply("Привет! Я бот-переводчик. Выберите язык, с которого нужно будет переводить", reply_markup=keyboards.initial_keyboard)


# Обработчик всех текстовых сообщений
@dp.message(F.text)
async def echo_message(message: Message):
    await message.answer(f"Я вас не понимаю")


@dp.callback_query(F.data == 'rus')
async def rus_lang(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Выбран русский язык')


@dp.callback_query(F.data == 'kubach')
async def rus_lang(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Выбран кубачинский язык')


# Функция для запуска бота
async def main():
    # Старт бота
    logging.info("Starting bot...")
    await dp.start_polling(bot)
    logging.info("Bot started!")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f'Ошибка {e}')