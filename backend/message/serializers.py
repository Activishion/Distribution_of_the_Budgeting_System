from typing import List

from rest_framework.serializers import ModelSerializer

from account.models import User
from message.models import Message


class UserMessageSerializer(ModelSerializer):
    class Meta:
        model: User = User
        depth: int = 1
        fields: List[str] = ['id', 'email', 'username']


class MessageSerializer(ModelSerializer):
    author = UserMessageSerializer(many=False, read_only=True)

    class Meta:
        model: Message = Message
        fields: List[str] = ['id', 'date', 'PAO', 'DZO', 'subject', 'message', 'author']
