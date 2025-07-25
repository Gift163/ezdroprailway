import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("🚀 Welcome to EZDROP!\n\nOpen amazing cases and earn rewards!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)