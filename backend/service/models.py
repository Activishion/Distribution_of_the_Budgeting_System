from typing import List

from django.db.models import (Model, ForeignKey, CharField, BooleanField, 
    DateTimeField, TextField, CASCADE)

from account.models import UserModel


class Message(Model):
    date = DateTimeField(auto_now_add=True)
    PAO = BooleanField(default=True)
    DZO = BooleanField(default=True)
    subject = CharField(max_length=255)
    message = TextField()
    author = ForeignKey(UserModel, on_delete=CASCADE)

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
    email = ForeignKey(UserModel, verbose_name='Email пользователя', on_delete=CASCADE)
    subscription = BooleanField('Подписка', default=False)

    def __str__(self) -> str:
        return f"{self.email} - {self.subscription}"


REPORT = (
    ('RTK', 'Прибыли и убытки РТК'),
    ('TEL', 'РТК + Tele2'),
    ('REP', 'Сегментная отчетность')
)

class Reporting(Model):
    report = CharField(max_length=100, choices=REPORT)
    email = ForeignKey(UserModel, verbose_name='Email пользователя', on_delete=CASCADE)
    subscription = BooleanField('Подписка', default=False)

    def __str__(self) -> str:
        return f"{self.email} - {self.report} - {self.subscription}"
