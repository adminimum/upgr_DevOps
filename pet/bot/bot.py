import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart

from keyboards.main_menu import main_menu
from handlers import (
    catalog,
    profile,
    info,
    purchases,
    delivery,
    work,
    operator,
    referral,
    balance,
)

def load_token() -> str:
    with open("token", "r") as f:
        return f.read().strip()

async def start_handler(message: Message):
    photo = FSInputFile("assets/menu.webp")

    text = (
        "👋 Добро пожаловать.\n\n"
        "🔹Отвечаем за качество.\n\n"
        "🔹Работаем круглосуточно.\n\n"
        "🔹Бонусная система начисления.\n\n"
        "🔹Реферальная система."
    )

    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=main_menu
    )

async def main():
    bot = Bot(token=load_token())
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.register(start_handler, CommandStart())

    # регистрация модулей
    catalog.register(dp)
    profile.register(dp)
    info.register(dp)
    purchases.register(dp)
    delivery.register(dp)
    work.register(dp)
    operator.register(dp)
    referral.register(dp)
    balance.register(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
