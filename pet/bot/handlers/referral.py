from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def referral_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("referral")

def register(dp: Dispatcher):
    dp.callback_query.register(referral_handler, F.data == "referral")
