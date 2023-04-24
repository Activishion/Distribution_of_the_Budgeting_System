from typing import List

from rest_framework.serializers import ModelSerializer

from account.models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model: UserModel = UserModel
        fields: str = '__all__'
