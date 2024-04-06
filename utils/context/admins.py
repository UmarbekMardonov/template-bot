from users.models import User
from utils.bot import bot
from asgiref.sync import sync_to_async


async def admin_start_send_message(user):
    admins = await sync_to_async(list)(User.objects.filter(is_admin=True))
    for admin in admins:
        # if admin.language == 'uz':
        if user.username:
            await bot.send_message(chat_id=admin.user_id, text=f"Botga @{user.username} qo'shildi!")
        else:
            await bot.send_message(chat_id=admin.user_id, text=f"Botga {user.first_name} qo'shildi!")
