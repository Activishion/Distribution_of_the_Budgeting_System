from typing import List

from django.db.models import (Model, CharField, BooleanField, TextField,
    DateTimeField)


class Message(Model):
    date = DateTimeField(auto_now_add=True)
    PAO = BooleanField(default=True)
    DZO = BooleanField(default=True)
    subject = CharField(max_length=255)
    message = TextField()
    author = CharField(max_length=100)
    full_name = CharField(max_length=200)

    class Meta:
        verbose_name: str = 'message'
        verbose_name_plural: str = 'messages'
        ordering: List[str] = ['-date', ]

    def __str__(self) -> str:
        return self.subject


class News(Model):
    user = CharField(max_length=100)
    full_name = CharField(max_length=200)
    subscription = BooleanField(default=False)

    class Meta:
        verbose_name: str = 'subscription'
        verbose_name_plural: str = 'news subscription'

    def __str__(self):
        if self.subscription == False:
            return f"Unsubscription - {self.user}"
        return f"Subscription - {self.user}"


REPORT = (
    ('Прибыли и убытки РТК', 'Прибыли и убытки РТК'),
    ('РТК + Tele2', 'РТК + Tele2'),
    ('Сегментная отчетность', 'Сегментная отчетность')
)

class Reporting(Model):
    report = CharField(max_length=100, choices=REPORT)
    user = CharField('User mail', max_length=100)
    full_name = CharField(max_length=200)
    subscription = BooleanField(default=False)
    data = DateTimeField(auto_now_add=True)

    """ Create """
    date_create = DateTimeField( auto_now_add=True)
    added_via_portal = BooleanField(default=True)

    """ Moderation """
    moderator_is_decision = BooleanField(default=False)
    moderator = CharField(max_length=100, blank=True, null=True)
    data_moderation = DateTimeField(blank=True, null=True)
    comment = TextField(blank=True, null=True)

    """ Delete """
    date_delete = DateTimeField(blank=True, null=True)
    comment_delete = TextField(blank=True, null=True)

    class Meta:
        verbose_name: str = 'reporting'
        verbose_name_plural: str = 'reportings'
        ordering: List[str] = ['-data', ]

    def __str__(self) -> str:
        return f"{self.user} - {self.report} - {self.subscription}"
