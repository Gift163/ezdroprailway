import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🎁 Welcome to EZDROP!
Play, win, and earn $EZCOIN!

💎 Try your luck now!", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("💼 Open WebApp")))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
