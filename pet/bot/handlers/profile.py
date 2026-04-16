from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def profile_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("profile")

def register(dp: Dispatcher):
    dp.callback_query.register(profile_handler, F.data == "profile")
