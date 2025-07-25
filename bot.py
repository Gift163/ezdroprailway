import os
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("🎉 Welcome to EZDROP! Open cases, win NFT items and earn $EZCOIN.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
