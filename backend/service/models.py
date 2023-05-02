from typing import List

from django.db.models import (Model, ForeignKey, CharField, BooleanField, 
    DateTimeField, TextField, CASCADE)

from account.models import UserModel


class Message(Model):
    date = DateTimeField('Дата', auto_now_add=True)
    PAO = BooleanField('ПАО', default=True)
    DZO = BooleanField('ДЗО', default=True)
    subject = CharField('Тема', max_length=255)
    message = TextField('Текст сообщения')
    author = ForeignKey(UserModel, verbose_name='Отправитель', on_delete=CASCADE)

    class Meta:
        verbose_name: str = 'сообщение'
        verbose_name_plural: str = 'сообщения'
        ordering: List[str] = ['-date', ]

    def __str__(self) -> str:
        return self.subject


class News(Model):
    user = ForeignKey(
        UserModel,
        related_name='newsUser',
        verbose_name='Пользователь',
        on_delete=CASCADE
    )
    subscription = BooleanField('Подписка', default=False)

    class Meta:
        verbose_name: str = 'новость'
        verbose_name_plural: str = 'новости'

    def __str__(self) -> str:
        return f"{self.subscription}"


REPORT = (
    ('Прибыли и убытки РТК', 'Прибыли и убытки РТК'),
    ('РТК + Tele2', 'РТК + Tele2'),
    ('Сегментная отчетность', 'Сегментная отчетность')
)

class Reporting(Model):
    report = CharField('Отчет', max_length=100, choices=REPORT)
    user = ForeignKey(UserModel, verbose_name='Email пользователя', on_delete=CASCADE)
    subscription = BooleanField('Подписка', default=False)
    data = DateTimeField('Дата заявки', auto_now_add=True)

    class Meta:
        verbose_name: str = 'подписку'
        verbose_name_plural: str = 'подписки'

    def __str__(self) -> str:
        return f"{self.user} - {self.report} - {self.subscription}"
