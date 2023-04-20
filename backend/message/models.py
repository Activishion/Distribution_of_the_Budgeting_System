from typing import List

from django.db.models import (Model, ForeignKey, CharField, BooleanField, 
    DateTimeField, TextField, CASCADE)

from account.models import User


class Message(Model):
    date = DateTimeField(auto_now_add=True)
    PAO = BooleanField(default=True)
    DZO = BooleanField(default=True)
    subject = CharField(max_length=255)
    message = TextField()
    author = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        verbose_name: str = 'сообщение'
        verbose_name_plural: str = 'сообщения'
        ordering: List[str] = ['-date', ]

    def __str__(self) -> str:
        return self.subject
