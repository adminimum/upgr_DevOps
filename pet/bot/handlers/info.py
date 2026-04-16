from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def info_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("info")

def register(dp: Dispatcher):
    dp.callback_query.register(info_handler, F.data == "info")
