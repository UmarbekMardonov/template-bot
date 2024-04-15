from users.models import User
from celery import shared_task
from asgiref.sync import sync_to_async
from utils.bot import bot
from config.celery import app

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def tasks():
    logger.info("Bu xabar 1 daqiqada bir marta chiqariladi!")


# tg_bot/tasks.py
#
# @app.task
# def my_task():
#     print("Bu mening birinchi Celery task'im!")
