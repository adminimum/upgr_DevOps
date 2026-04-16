from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def balance_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("balance")

def register(dp: Dispatcher):
    dp.callback_query.register(balance_handler, F.data == "balance")
