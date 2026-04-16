from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

async def work_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("work")

def register(dp: Dispatcher):
    dp.callback_query.register(work_handler, F.data == "work")
