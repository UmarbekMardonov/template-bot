from telegram import Update
from telegram.ext import ContextTypes
from users.models import User
from utils.bot import bot
from asgiref.sync import sync_to_async
from tg_bot.handlers.admins.keyboards_a import admin_func
from tg_bot import states
from utils.context import users


async def admin_func_hand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admins = await sync_to_async(list)(User.objects.filter(is_admin=True))
    for admin in admins:
        if admin.user_id == update.message.from_user.id:
            keyboard = await admin_func()
            await bot.send_message(chat_id=update.message.from_user.id, text="Admin funksiyasi!",
                                   reply_markup=keyboard)
    return states.MENU_ADMIN


async def count_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = await sync_to_async(list)(User.objects.all())
    count = len(users)
    await bot.send_message(chat_id=update.callback_query.from_user.id, text=f'{count} users')
    return states.MAIN_MENU


async def message_text_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await bot.send_message(chat_id=update.callback_query.from_user.id, text='send message to me for users')
    return states.MESSAGE_USERS


async def send_message_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admin = await sync_to_async(User.objects.get)(user_id=update.message.from_user.id)
    users_all = await sync_to_async(list)(User.objects.all())
    for user in users_all:
        try:
            if update.message.video:
                video_id = update.message.video.file_id
                caption = update.message.caption
                await bot.send_video(chat_id=user.user_id, caption=caption, video=video_id)
            elif update.message.photo:
                photo_id = update.message.photo[-1].file_id
                caption = update.message.caption
                await bot.send_photo(chat_id=user.user_id, caption=caption, photo=photo_id)
            elif update.message.text:
                await bot.send_message(chat_id=user.user_id, text=update.message.text)
        except Exception as e:
            if "Unauthorized" in str(e):
                user.delete()
    user = admin
    text = await users.menu(user)
    await bot.send_message(chat_id=update.message.from_user.id, text=text)
    return states.MAIN_MENU


async def message_text_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await bot.send_message(chat_id=update.callback_query.from_user.id, text='send message to me for a user')
    return states.MESSAGE_USER


async def send_message_a_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message.video:
            video_id = update.message.video.file_id
            text = update.message.caption
            text = text.split(" ")
            user_id = text[0]
            text.remove(text[0])
            text = " ".join(text)
            await bot.send_video(chat_id=user_id, caption=text, video=video_id)
        elif update.message.photo:
            photo_id = update.message.photo[-1].file_id
            text = update.message.caption
            text = text.split(" ")
            user_id = text[0]
            text.remove(text[0])
            text = " ".join(text)
            await bot.send_photo(chat_id=user_id, caption=text, photo=photo_id)
        elif update.message.text:
            text = update.message.text
            text = text.split(" ")
            user_id = text[0]
            text.remove(text[0])
            text = " ".join(text)
            await bot.send_message(chat_id=user_id, text=text)
    except Exception as e:
        if "Unauthorized" in str(e):
            admin = await sync_to_async(User.objects.get)(user_id=update.message.from_user.id)  # admin
            await bot.send_message(chat_id=admin.user_id, text='Unauthorized error')
    user = await sync_to_async(User.objects.get)(user_id=update.message.from_user.id)  # admin
    text = await users.menu(user)
    await bot.send_message(chat_id=update.message.from_user.id, text=text)
    return states.MAIN_MENU
