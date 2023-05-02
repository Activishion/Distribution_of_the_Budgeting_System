from typing import List
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField

from account.models import UserModel
from account.serializers import UserSerializer
from service.models import Message, News, Reporting
from django.shortcuts import get_object_or_404


class UserMessageSerializer(ModelSerializer):
    class Meta:
        model: UserModel = UserModel
        depth: int = 1
        fields: List[str] = ['full_name', ]


class UserReportSerializer(ModelSerializer):
    class Meta:
        model: UserModel = UserModel
        depth: int = 1
        fields: List[str] = ['email', 'full_name']


class MessageSerializer(ModelSerializer):
    author = UserMessageSerializer(many=False, read_only=True)

    class Meta:
        model: Message = Message
        fields: List[str] = ['id', 'date', 'PAO', 'DZO', 'subject', 
            'message', 'author']


class UserForEmailReport(ModelSerializer):
    class Meta:
        model: UserModel = UserModel
        fields: List[str] = ['email', ]


class NewsSerializer(ModelSerializer):
    user = UserReportSerializer(many=True, required=True)
    subscription = CharField()

    class Meta:
        model: News = News
        fields: List[str] = ['id', 'user', 'subscription']

    def validate(self, data):
        if data['subscription'] == 'Подписаться':
            data['subscription'] = True
        if data['subscription'] == 'Отписаться':
            data['subscription'] = False
        # print(data)
        return data


class ReportSerializer(ModelSerializer):
    email = CharField(required=True, source='user.email')
    subscription = CharField()

    class Meta:
        model: Reporting = Reporting
        fields: List[str] = ['id', 'report', 'email', 'subscription', 'data']

    def validate(self, data):
        if data['subscription'] == 'Подписаться':
            data['subscription'] = True
        if data['subscription'] == 'Отписаться':
            data['subscription'] = False
        print(data)
        return data

    def create(self, validated_data):
        return Reporting.objects.create(**validated_data)


class PostReportSerializer(serializers.Serializer):
    report = serializers.CharField()
    email = serializers.EmailField(source='user.email')
    subscription = serializers.CharField()

    def validate(self, data):
        if data['subscription'] == 'Подписаться':
            data['subscription'] = True
        if data['subscription'] == 'Отписаться':
            data['subscription'] = False
        return data

    def create(self, validated_data):
        email = validated_data['user']['email']
        subscription = validated_data['subscription']
        report = validated_data['report']
        user = get_object_or_404(UserModel, email=email)
        return Reporting.objects.create(
            user=user,
            report=report,
            subscription=subscription
        )


class PostNewsSerializer(serializers.Serializer):
    email = serializers.EmailField(source='user.email')
    subscription = serializers.CharField()

    def validate(self, data):
        if data['subscription'] == 'Подписаться':
            data['subscription'] = True
        if data['subscription'] == 'Отписаться':
            data['subscription'] = False
        return data

    def create(self, validated_data):
        email = validated_data['user']['email']
        subscription = validated_data['subscription']
        user = get_object_or_404(UserModel, email=email)
        return News.objects.create(
            user=user,
            subscription=subscription
        )