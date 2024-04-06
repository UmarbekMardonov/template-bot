from users.models import User
from utils.bot import bot


async def users_start(user):
    text = (f"Assalomu Alaykum {user.first_name}\n Botga xo'sh kelibsiz! Tilni tanlang 👇\n"
            f" Welcome to the bot! Choose language 👇 \n Добро пожаловать в бот! Выберите язык 👇")
    return text


async def users_start_retry(user):
    if user.language == 'en':
        text = f"{user.first_name} glad you're back the bot! 😊 Choose language 👇"
    elif user.language == 'ru':
        text = f"{user.first_name} рад, что ты вернулся в бот! 😊 Выберите язык 👇"
    else:
        text = f"{user.first_name} botga qaytganizdan xursandman! 😊 Tilni tanlang 👇"
    return text


async def users_start_not_language(user):
    if user.language == 'en':
        text = f"{user.first_name} glad you're back the bot! 😊"
    elif user.language == 'ru':
        text = f"{user.first_name} рад, что ты вернулся в бот! 😊"
    else:
        text = f"{user.first_name} botga qaytganizdan xursandman! 😊"
    return text


async def menu(user):
    if user.language == 'en':
        text = "You are in the main menu."
    elif user.language == 'ru':
        text = "Вы находитесь в главном меню."
    else:
        text = "Siz asosiy menyudasiz."
    return text


async def choose_language_text(user):
    if user.language == 'en':
        text = "Choose language. 👇"
    elif user.language == 'ru':
        text = "Выберите язык. 👇"
    else:
        text = "Tilni tanlang. 👇"
    return text
