import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🌷 Добро пожаловать в Flower Profit AI\n\n"
        "Напишите /neworder для создания заказа."
    )

@dp.message()
async def echo(message: Message):
    if message.text == "/neworder":
        await message.answer(
            "Кому подарок?\n\n"
            "👩 Девушке\n"
            "👨 Мужчине\n"
            "👶 Ребёнку\n"
            "👩‍🦳 Маме"
        )

async def main():
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
