from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import UserModel
from service.models import News, Reporting


@receiver(post_save, sender=Reporting)
@receiver(post_save, sender=News)
def post_user_save(instance, **kwargs):
    email = instance.user
    full_name = instance.full_name

    user = UserModel.objects.filter(email=email)
    if len(user) == 0:
        new_user = UserModel(
            email=email,
            full_name=full_name,
            is_active=True,
            is_admin=False,
            is_superuser=False
        )
        new_user.save()
