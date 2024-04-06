from telegram import Update
from telegram.ext import ContextTypes
from users.models import User
from utils.bot import bot
from utils.context import users
from utils.context.admins import admin_start_send_message
from tg_bot.handlers.users.keyboards import choose_language, main_menu
from tg_bot import states
from asgiref.sync import sync_to_async


async def command_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user, created = await User.get_or_create(update, context)
    lang = await choose_language()
    if created:
        text = await users.users_start(user)
        await admin_start_send_message(user)
        await bot.send_message(chat_id=update.message.from_user.id, text=text, reply_markup=lang)

    else:
        text_start_retry = await users.users_start_retry(user)
        text_not_language = await users.users_start_not_language(user)
        if user.language:
            reply_markup = await main_menu()
            await bot.send_message(chat_id=update.message.from_user.id, text=text_not_language,
                                   reply_markup=reply_markup)
            return states.MAIN_MENU
        else:
            await bot.send_message(chat_id=update.message.from_user.id, text=text_start_retry, reply_markup=lang)
    return states.CHOOSE_LANG


async def language_choose(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user = await User.get_user_with_user_id(user_id)
    text = await users.choose_language_text(user)
    reply_markup = await choose_language()
    await bot.send_message(chat_id=user_id, text=text, reply_markup=reply_markup)
    return states.CHOOSE_LANG


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.callback_query.from_user.id
    user = await User.get_user_with_user_id(user_id)
    user.language = update.callback_query.data
    await sync_to_async(user.save)()
    text = await users.menu(user)
    reply_markup = await main_menu()
    await bot.send_message(chat_id=user_id, text=text, reply_markup=reply_markup)
    return states.MAIN_MENU
