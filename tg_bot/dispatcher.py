"""
    Telegram event handlers
"""
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters
)
from telegram.ext._handlers.callbackqueryhandler import CallbackQueryHandler

from config.settings import DEBUG
from tg_bot.handlers.users import handlers, keyboards
from tg_bot import states
from tg_bot.handlers.admins import handlers_a, keyboards_a


def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """
    conv = ConversationHandler(
        entry_points=[CommandHandler('start', handlers.command_start)],
        states={
            states.MAIN_MENU: [
                CommandHandler('me', handlers_a.admin_func_hand),
                MessageHandler(filters.Regex(f"^{keyboards.CHOOSE_LANGUAGE}"),
                               handlers.language_choose),

            ],
            states.CHOOSE_LANG: [
                CallbackQueryHandler(handlers.menu, pattern='^uz|ru|en$'),
            ],
            states.MENU_ADMIN: [
                CallbackQueryHandler(handlers_a.count_users, pattern=f'^{keyboards_a.COUNT_USERS}$'),
                CallbackQueryHandler(handlers_a.message_text_users,
                                     pattern=f'^{keyboards_a.SEND_MESSAGE_USERS}$'),
                CallbackQueryHandler(handlers_a.message_text_user,
                                     pattern=f'^{keyboards_a.SEND_MESSAGE_USER}$'),
            ],
            states.MESSAGE_USERS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND
                               | filters.PHOTO
                               | filters.VIDEO
                               | filters.CAPTION, handlers_a.send_message_users)
            ],

            states.MESSAGE_USER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND
                               | filters.PHOTO
                               | filters.VIDEO
                               | filters.CAPTION, handlers_a.send_message_a_user)
            ],
        },
        fallbacks=[CommandHandler('start', handlers.command_start)],

    )
    dp.add_handler(conv)
    # dp.add_handler(CommandHandler("start", handlers.command_start))

    # admins
    # dp.add_handler(CommandHandler("me", handlers_a.admin_func_hand))

    # handling errors
    # dp.add_error_handler(error.send_stacktrace_to_tg_chat)

    return dp


n_workers = 0 if DEBUG else 4
application = ApplicationBuilder().token("7156339416:AAE3pnsU6BalRw4EBSxz6xY3RjlqcdDBYek").build()
