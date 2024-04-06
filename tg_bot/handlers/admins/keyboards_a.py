from telegram import InlineKeyboardMarkup, InlineKeyboardButton

COUNT_USERS = 'count users'
SEND_MESSAGE_USER = 'send message a user'
SEND_MESSAGE_USERS = 'send message users'


async def admin_func():
    keyboard = [
        [
            InlineKeyboardButton(COUNT_USERS, callback_data=COUNT_USERS),
            InlineKeyboardButton(SEND_MESSAGE_USER, callback_data=SEND_MESSAGE_USER),
        ],
        [
            InlineKeyboardButton(SEND_MESSAGE_USERS, callback_data=SEND_MESSAGE_USERS),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup
