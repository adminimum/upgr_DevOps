# import random

# from aiogram import Dispatcher, F
# from aiogram.types import (
#     CallbackQuery,
#     Message,
#     ReplyKeyboardRemove,
#     InlineKeyboardMarkup,
#     InlineKeyboardButton,
# )
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext

# from configs.cities import cities
# from configs.shops import shops


# class CatalogState(StatesGroup):
#     waiting_for_city = State()
#     waiting_for_shop = State()


# def build_shops_keyboard() -> InlineKeyboardMarkup:
#     shuffled = shops[:]
#     random.shuffle(shuffled)

#     keyboard = [
#         [InlineKeyboardButton(text=shop, callback_data=f"shop:{shop}")]
#         for shop in shuffled
#     ]

#     return InlineKeyboardMarkup(inline_keyboard=keyboard)


# async def catalog_start(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()

#     # убираем inline-меню под сообщением
#     await callback.message.edit_reply_markup(reply_markup=None)

#     await state.set_state(CatalogState.waiting_for_city)

#     await callback.message.answer(
#         "Введите город:",
#         reply_markup=ReplyKeyboardRemove()
#     )


# async def city_input(message: Message, state: FSMContext):
#     user_city = message.text.strip().lower()
#     cities_lower = [c.lower() for c in cities]

#     if user_city not in cities_lower:
#         await message.answer(
#             "❌ Город не найден.\n"
#             "Проверьте написание и попробуйте снова."
#         )
#         return

#     city_normalized = cities[cities_lower.index(user_city)]

#     await state.update_data(city=city_normalized)
#     await state.set_state(CatalogState.waiting_for_shop)

#     await message.answer(
#         f"Город: {city_normalized}\n\nВыберите магазин:",
#         reply_markup=build_shops_keyboard()
#     )


# async def shop_selected(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()

#     shop_name = callback.data.split("shop:", 1)[1]
#     data = await state.get_data()
#     city = data.get("city")

#     await state.clear()

#     await callback.message.edit_reply_markup(reply_markup=None)

#     await callback.message.answer(
#         f"✅ Вы выбрали:\n"
#         f"Город: {city}\n"
#         f"Магазин: {shop_name}"
#     )


# def register(dp: Dispatcher):
#     dp.callback_query.register(catalog_start, F.data == "catalog")
#     dp.message.register(city_input, CatalogState.waiting_for_city)
#     dp.callback_query.register(
#         shop_selected,
#         CatalogState.waiting_for_shop,
#         F.data.startswith("shop:")
#     )

import random

from aiogram import Dispatcher, F
from aiogram.types import (
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from configs.cities import cities
from configs.shops import shops


class CatalogState(StatesGroup):
    waiting_for_city = State()
    waiting_for_shop = State()


def build_shops_keyboard() -> InlineKeyboardMarkup:
    shuffled = shops[:]
    random.shuffle(shuffled)

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=shop, callback_data=f"shop:{shop}")]
            for shop in shuffled
        ]
    )


async def catalog_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    await state.set_state(CatalogState.waiting_for_city)

    await callback.message.edit_caption(
        caption=(
            "👋 Добро пожаловать.\n\n"
            "🔹Отвечаем за качество.\n\n"
            "🔹Работаем круглосуточно.\n\n"
            "🔹Бонусная система начисления.\n\n"
            "🔹Реферальная система.\n\n"
            "━━━━━━━━━━━━━━\n"
            "Введите город:"
        ),
        reply_markup=None
    )


async def city_input(message: Message, state: FSMContext):
    user_city = message.text.strip().lower()
    cities_lower = [c.lower() for c in cities]

    if user_city not in cities_lower:
        await message.answer("❌ Город не найден. Попробуйте снова.")
        return

    city_normalized = cities[cities_lower.index(user_city)]

    await state.update_data(city=city_normalized)
    await state.set_state(CatalogState.waiting_for_shop)

    # редактируем ПОСЛЕДНЕЕ сообщение бота с картинкой
    await message.bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=message.reply_to_message.message_id
        if message.reply_to_message
        else message.message_id - 1,
        caption=(
            f"📍 Город: {city_normalized}\n\n"
            "Выберите магазин:"
        ),
        reply_markup=build_shops_keyboard()
    )


async def shop_selected(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    shop_name = callback.data.split("shop:", 1)[1]
    data = await state.get_data()
    city = data.get("city")

    await state.clear()

    await callback.message.edit_caption(
        caption=(
            f"✅ Вы выбрали:\n\n"
            f"📍 Город: {city}\n"
            f"🏪 Магазин: {shop_name}"
        ),
        reply_markup=None
    )


def register(dp: Dispatcher):
    dp.callback_query.register(catalog_start, F.data == "catalog")
    dp.message.register(city_input, CatalogState.waiting_for_city)
    dp.callback_query.register(
        shop_selected,
        CatalogState.waiting_for_shop,
        F.data.startswith("shop:")
    )
