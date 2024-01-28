from aiogram import Bot, Dispatcher, types
import logging
import asyncio
from aiogram.filters.command import Command
import setting

logging.basicConfig(level=logging.INFO)

bot = Bot(token=setting.token)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}. \nI am bot")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


