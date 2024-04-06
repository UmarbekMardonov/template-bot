from django.db import models
from utils.models import nb
from telegram import Update
from telegram.ext import CallbackContext
from utils.models import user_get_data
from asgiref.sync import sync_to_async


class User(models.Model):
    user_id = models.PositiveBigIntegerField(primary_key=True)  # telegram_id
    username = models.CharField(max_length=32, **nb)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, **nb)
    language_code = models.CharField(max_length=8, help_text="Telegram client's lang", **nb)
    deep_link = models.CharField(max_length=64, **nb)
    language = models.CharField(max_length=20, **nb)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    @classmethod
    async def get_or_create(cls, update: Update, context: CallbackContext):
        data = user_get_data(update)
        user, created = await sync_to_async(cls.objects.update_or_create)(user_id=data["user_id"], defaults=data)
        if created:
            if context is not None and context.args is not None and len(context.args) > 0:
                payload = context.args[0]
                if str(payload).strip() != str(data["user_id"]).strip():
                    user.deep_link = payload
                    await sync_to_async(user.save)()
        return user, created

    @classmethod
    async def get_user_with_user_id(cls, user_id):
        user = await sync_to_async(cls.objects.get)(user_id=user_id)
        return user

    @classmethod
    async def admins_list(cls):
        admins = await sync_to_async(cls.objects.filter)(is_admin=True)
        return admins

