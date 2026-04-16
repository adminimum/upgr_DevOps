from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def operator_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("operator")

def register(dp: Dispatcher):
    dp.callback_query.register(operator_handler, F.data == "operator")
