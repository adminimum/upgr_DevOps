from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def delivery_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("delivery")

def register(dp: Dispatcher):
    dp.callback_query.register(delivery_handler, F.data == "delivery")
