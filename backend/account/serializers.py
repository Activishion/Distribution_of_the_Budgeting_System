from typing import List

from rest_framework.serializers import ModelSerializer

from account.models import UserModel


class SubscriptionСheck(ModelSerializer):
    class Meta:
        model: UserModel = UserModel
        fields: List[str] = ['email', ]
