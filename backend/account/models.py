from django.contrib.auth.models import User
from django.db.models import (Model, CharField, BooleanField, 
    DateTimeField, TextField, OneToOneField, ForeignKey, CASCADE)
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    external = BooleanField(default=False)

    """ Create """
    date_create = DateTimeField('Дата добавления', auto_now_add=True)
    added_via_portal = BooleanField('Добавлено через портал', default=True)

    """ Moderation """
    moderator_is_decision = BooleanField('Проверка модератора', default=False)
    moderator = CharField('Модератор', max_length=100, blank=True, null=True)
    data_moderation = DateTimeField('Дата модерации', blank=True, null=True)
    comment = TextField('Комментарий модератора', blank=True, null=True)

    """ Delete """
    date_delete = DateTimeField('Дата удаления', blank=True, null=True)
    comment_delete = TextField('Комментарий при удалении', blank=True, null=True)

    class Meta:
        verbose_name: str = 'пользователь'
        verbose_name_plural: str = 'пользователи'

    def __str__(self) -> str:
        return self.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class News(Model):
    user = ForeignKey(Profile, verbose_name='Пользователь', on_delete=CASCADE)
    email = ForeignKey(Profile, verbose_name='Email пользователя', on_delete=CASCADE)
    subscription = BooleanField('Подписка', default=False)

    def __str__(self) -> str:
        return f"{self.email} - {self.subscription}"


REPORTS= (
    ('RTK', 'Прибыли и убытки РТК'),
    ('TEL', 'РТК + Tele2'),
    ('REP', 'Сегментная отчетность')
)

class Reporting(Model):
    report = CharField(max_length=100, choise = REPORTS)
    email = ForeignKey(Profile, verbose_name='Email пользователя', on_delete=CASCADE)
    subscription = BooleanField('Подписка', default=False)

    def __str__(self) -> str:
        return f"{self.email} - {self.report} - {self.subscription}"
