from typing import List

from rest_framework.serializers import ModelSerializer

from account.models import User, News, Reporting


class UserSerializer(ModelSerializer):
    class Meta:
        model: User = User
        fields: str = '__all__'


class NewsSerializer(ModelSerializer):
    class Meta:
        model: News = News
        fields: List[str] = ['id', 'email', 'subscription']


class ReportSerializer(ModelSerializer):
    class Meta:
        model: Reporting = Reporting
        fields: List[str] = ['id', 'report', 'email', 'subscription']
