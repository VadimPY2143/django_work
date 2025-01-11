from celery import shared_task
from users_app.models import User


@shared_task
def user_save_task(user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()



@shared_task
def user_delete_task(user_id):
    user = User.objects.get(id=user_id)
    user.delete()
