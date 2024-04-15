from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def choose_language():
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿", callback_data='uz'),
            InlineKeyboardButton("🇷🇺", callback_data='ru'),
            InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data='en'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


CHOOSE_LANGUAGE = "🔄 🇺🇿 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇷🇺"


async def main_menu():
    keyboard = [
        [
            KeyboardButton(text=CHOOSE_LANGUAGE, ),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
