import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from config.settings import TELEGRAM_TOKEN, SEND_MESSAGE_CHAT_ID
from telegram import Update, Bot
from telegram.ext import Application
from tg_bot.dispatcher import setup_dispatcher


def bot_run() -> None:
    """Start the bot."""
    dp = Application.builder().token(TELEGRAM_TOKEN).build()
    setup_dispatcher(dp)
    print(f"Bot started")
    dp.run_polling(allowed_updates=Update.ALL_TYPES)
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=SEND_MESSAGE_CHAT_ID, text="Bot ready!")


if __name__ == "__main__":
    bot_run()
