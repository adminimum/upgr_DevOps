from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def purchases_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("purchases")

def register(dp: Dispatcher):
    dp.callback_query.register(purchases_handler, F.data == "purchases")
