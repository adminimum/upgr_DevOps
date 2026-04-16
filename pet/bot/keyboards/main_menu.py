from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💊Каталог", callback_data="catalog"),
            InlineKeyboardButton(text="👨Профиль", callback_data="profile"),
        ],
        [
            InlineKeyboardButton(text="🗒️Информация", callback_data="info"),
        ],
        [
            InlineKeyboardButton(text="📦Мои покупки", callback_data="purchases"),
            InlineKeyboardButton(text="🚖Доставка", callback_data="delivery"),
        ],
        [
            InlineKeyboardButton(text="🔥Работа", callback_data="work"),
            InlineKeyboardButton(text="👨‍💻Оператор", callback_data="operator"),
        ],
        [
            InlineKeyboardButton(text="👥Реферальная система", callback_data="referral"),
        ],
        [
            InlineKeyboardButton(text="💵Пополнить баланс", callback_data="balance"),
        ],
    ]
)
