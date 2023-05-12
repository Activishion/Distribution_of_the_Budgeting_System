from typing import List

from rest_framework.serializers import ModelSerializer, CharField

from service.models import Message, News, Reporting


class MessageSerializer(ModelSerializer):
    class Meta:
        model: Message = Message
        fields: List[str] = ['id', 'date', 'PAO', 'DZO', 'subject', 
            'message', 'author', 'full_name']


class GetReportSerializer(ModelSerializer):
    subscription = CharField()

    class Meta:
        model: Reporting = Reporting
        fields: List[str] = ['id', 'report', 'full_name', 'user', 'subscription',
            'data', 'date_create', 'added_via_portal', 'moderator_is_decision',
            'moderator', 'data_moderation', 'comment', 'date_delete', 'comment_delete']

    def validate(self, data):
        if data['subscription'] == 'Подписаться':
            data['subscription'] = True
        if data['subscription'] == 'Отписаться':
            data['subscription'] = False
        return data

    def create(self, validated_data):
        return Reporting.objects.create(**validated_data)


class PostReportSerializer(ModelSerializer):
    subscription = CharField()
    user = CharField()

    class Meta:
        model: Reporting = Reporting
        fields: List[str] = ['report', 'full_name', 'user', 'subscription']

    def validate(self, data):
        if data['subscription'] == 'Подписаться':
            data['subscription'] = True
        if data['subscription'] == 'Отписаться':
            data['subscription'] = False
        return data


class GetNewsSerializer(ModelSerializer):
    class Meta:
        model: News = News
        fields: List[str] = ['id', 'full_name', 'user', 'subscription']


class PostNewsSerializer(ModelSerializer):
    subscription = CharField()

    class Meta:
        model: News = News
        fields: List[str] = ['full_name', 'user', 'subscription']

    def validate(self, data):
        if data['subscription'] == 'Подписаться':
            data['subscription'] = True
        if data['subscription'] == 'Отписаться':
            data['subscription'] = False
        return data
