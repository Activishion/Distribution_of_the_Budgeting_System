from typing import List

from rest_framework.serializers import ModelSerializer

from account.models import UserModel
from account.serializers import UserSerializer
from service.models import Message, News, Reporting


class UserMessageSerializer(ModelSerializer):
    class Meta:
        model: UserModel = UserModel
        depth: int = 1
        fields: List[str] = ['full_name', ]


class MessageSerializer(ModelSerializer):
    author = UserMessageSerializer(many=False, read_only=True)

    class Meta:
        model: Message = Message
        fields: List[str] = ['id', 'date', 'PAO', 'DZO', 'subject', 
            'message', 'author']


class NewsSerializer(ModelSerializer):
    class Meta:
        model: News = News
        fields: List[str] = ['id', 'email', 'subscription']


class ReportSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model: Reporting = Reporting
        fields: List[str] = ['id', 'report', 'user', 'subscription']
