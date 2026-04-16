# bot_inline.py

import asyncio
import random
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    FSInputFile,
)

def read_token():
    pass


#BOT_TOKEN = "8563764213:AAGWXsYFnfMZ1u1J1BgxWY6B_8PP4ZD9Oxs"

MENU_IMAGE_PATH = "menu.webp"

# ====== DATA ======

CITIES = {
    "москва", "санкт-петербург", "новосибирск", "екатеринбург", "казань",
    "нижний новгород", "челябинск", "красноярск", "самара", "уфа",
    "ростов-на-дону", "омск", "краснодар", "воронеж", "пермь",
    "волгоград", "тюмень", "ижевск", "барнаул", "ульяновск",
}

SHOPS = [
    "Лавка «Другое сознание»",
    "Love Store",
    "Stuffman",
    "[ЦУМ Россия] TOP 1 COCAINE!",
    "ПАВстанция",
    "CONGLOMERATE",
    "Юла",
    "7up market",
    "Sayonara",
    "БРОКЕР",
    "Makedonsky",
    "Nostradamus",
    "Национальный стандарт",
    "У Людочки",
    "StaffBerries",
    "Солевая Хата",
    "YAMAKASI",
    "Столичный",
    "✨ Бриз ✨",
    "Империя Соблазна",
    "Третий Рим",
    "Link",
    "BENJAMIN",
    "GangBang Shop",
    "Черкизон",
    "Burger King",
    "DENDI",
    "Секреты Счастья",
    "Карабас",
]

PRODUCTS = [
    "Амфетамин Premium",
    "Гашиш Static Sift",
    "Hash Ice-o-lator",
    "Critical Kush",
    "Метадон",
    "Кокаин",
    "★ОПТ★ Mephedrone crystal",
    "★ОПТ★ Alpha PvP цвет на ваш выбор",
    "Alpha PvP white crystal",
    "Mephedrone crystal",
    "Mephedrone crystal Luxe",
    "A-PVP Green Crystal",
    "A-PVP Blue Crystal",
]

WAITING_FOR_CITY = set()

WELCOME_TEXT = (
    "👋 Добро пожаловать\n\n"
    "🔹 Качество\n"
    "🔹 24/7\n"
    "🔹 Бонусы\n"
)

# ====== KEYBOARDS ======

def main_menu_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💊 Каталог", callback_data="catalog")],
        ]
    )


def shops_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    items = SHOPS[:]
    random.shuffle(items)

    for shop in items:
        kb.inline_keyboard.append(
            [InlineKeyboardButton(text=shop, callback_data="shop")]
        )

    kb.inline_keyboard.append(
        [InlineKeyboardButton(text="« Назад", callback_data="back_main")]
    )
    return kb


def products_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    items = PRODUCTS[:]
    random.shuffle(items)

    for product in items:
        kb.inline_keyboard.append(
            [InlineKeyboardButton(text=product, callback_data="product")]
        )

    kb.inline_keyboard.append(
        [InlineKeyboardButton(text="« Назад", callback_data="back_shops")]
    )
    return kb


# ====== START ======

async def show_main_menu(message: Message):
    photo = FSInputFile(MENU_IMAGE_PATH)
    await message.answer_photo(
        photo=photo,
        caption=WELCOME_TEXT,
        reply_markup=main_menu_kb(),
    )


async def cmd_start(message: Message):
    await show_main_menu(message)


# ====== CALLBACKS ======

async def on_click(callback: CallbackQuery):
    await callback.answer()
    uid = callback.from_user.id
    action = callback.data

    if action == "catalog":
        WAITING_FOR_CITY.add(uid)
        await callback.message.edit_caption(
            caption="📍 Введите город:",
            reply_markup=None,
        )
        return

    if action == "shop":
        await callback.message.edit_text(
            "📦 Выберите товар:",
            reply_markup=products_kb(),
        )
        return

    if action == "product":
        await callback.message.edit_text(
            "📦 Выберите товар:",
            reply_markup=products_kb(),  # снова тот же список, но перемешанный
        )
        return

    if action == "back_shops":
        await callback.message.edit_text(
            "🏪 Выберите магазин:",
            reply_markup=shops_kb(),
        )
        return

    if action == "back_main":
        await show_main_menu(callback.message)
        return


# ====== TEXT INPUT ======

async def on_text(message: Message):
    uid = message.from_user.id
    if uid not in WAITING_FOR_CITY:
        return

    city = message.text.strip().lower()
    if city not in CITIES:
        await message.answer("❌ Город не найден. Повторите.")
        return

    WAITING_FOR_CITY.remove(uid)

    await message.answer(
        f"✅ Город принят\n\n🏪 Выберите магазин:",
        reply_markup=shops_kb(),
    )


# ====== MAIN ======

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(cmd_start, F.text.in_({"/start", "/menu"}))
    dp.callback_query.register(on_click)
    dp.message.register(on_text)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
