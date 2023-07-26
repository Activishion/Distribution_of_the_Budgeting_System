from typing import List

from django.db.models import (Model, CharField, BooleanField, TextField,
    DateTimeField)


class Message(Model):
    date = DateTimeField('Дата', auto_now_add=True)
    PAO = BooleanField('ПАО', default=True)
    DZO = BooleanField('ДЗО', default=True)
    subject = CharField('Тема', max_length=255)
    message = TextField('Текст сообщения')
    author = CharField('Отправитель', max_length=100)
    full_name = CharField('ФИО', max_length=200)

    class Meta:
        verbose_name: str = 'сообщение'
        verbose_name_plural: str = 'сообщения'
        ordering: List[str] = ['-date', ]

    def __str__(self) -> str:
        return self.subject


class News(Model):
    user = CharField('Пользователь', max_length=100)
    full_name = CharField('ФИО', max_length=200)
    subscription = BooleanField('Подписка', default=False)

    class Meta:
        verbose_name: str = 'подписку'
        verbose_name_plural: str = 'подписки на новости'

    def __str__(self):
        if self.subscription == False:
            return f"Отписка - {self.user}"
        return f"Подписка - {self.user}"


REPORT = (
    ('Прибыли и убытки РТК', 'Прибыли и убытки РТК'),
    ('РТК + Tele2', 'РТК + Tele2'),
    ('Сегментная отчетность', 'Сегментная отчетность')
)

class Reporting(Model):
    report = CharField('Отчет', max_length=100, choices=REPORT)
    user = CharField('Email пользователя', max_length=100)
    full_name = CharField('ФИО', max_length=200)
    subscription = BooleanField('Подписка', default=False)
    data = DateTimeField('Дата заявки', auto_now_add=True)

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
        verbose_name: str = 'отчетность'
        verbose_name_plural: str = 'отчетности'
        ordering: List[str] = ['-data', ]

    def __str__(self) -> str:
        return f"{self.user} - {self.report} - {self.subscription}"
