# bot_inline.py

import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    FSInputFile,
)

# ====== CONFIG ======

BOT_TOKEN = "8563764213:AAGWXsYFnfMZ1u1J1BgxWY6B_8PP4ZD9Oxs"
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

WAITING_FOR_CITY = set()

WELCOME_TEXT = (
    "👋 Добро пожаловать.\n\n"
    "🔹 Отвечаем за качество\n"
    "🔹 Работаем круглосуточно\n"
    "🔹 Бонусная система\n"
    "🔹 Реферальная программа"
)

# ====== KEYBOARDS ======

def main_menu_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💊 Каталог", callback_data="catalog"),
                InlineKeyboardButton(text="🧑‍💼 Профиль", callback_data="profile"),
            ],
            [InlineKeyboardButton(text="📄 Информация", callback_data="info")],
        ]
    )


def shops_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    items = SHOPS[:]
    random.shuffle(items)

    for shop in items:
        kb.inline_keyboard.append(
            [InlineKeyboardButton(text=shop, callback_data=f"shop:{shop}")]
        )

    kb.inline_keyboard.append(
        [InlineKeyboardButton(text="« Назад", callback_data="back")]
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
            caption="📍 Введите ваш город:",
            reply_markup=None,
        )
        return

    if action == "back":
        await show_main_menu(callback.message)
        return

    if action.startswith("shop:"):
        shop = action.split(":", 1)[1]
        await callback.message.edit_text(
            f"🏪 Вы выбрали магазин:\n\n<b>{shop}</b>",
            parse_mode="HTML",
        )
        return

    texts = {
        "profile": "🧑‍💼 Профиль пользователя",
        "info": "📄 Информация и правила",
    }

    await callback.message.edit_caption(
        caption=texts.get(action, "Неизвестный пункт"),
        reply_markup=main_menu_kb(),
    )


# ====== TEXT INPUT ======

async def on_text(message: Message):
    uid = message.from_user.id
    if uid not in WAITING_FOR_CITY:
        return

    city = message.text.strip().lower()

    if city not in CITIES:
        await message.answer("❌ Город не найден. Попробуйте ещё раз.")
        return

    WAITING_FOR_CITY.remove(uid)

    await message.answer(
        f"✅ Город <b>{message.text}</b> принят.\n\nВыберите магазин:",
        reply_markup=shops_kb(),
        parse_mode="HTML",
    )


# ====== MAIN ======

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(cmd_start, F.text.in_({"/start", "/menu"}))
    dp.callback_query.register(on_click)
    dp.message.register(on_text)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
