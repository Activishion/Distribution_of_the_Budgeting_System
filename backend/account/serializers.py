from typing import List

from rest_framework.serializers import ModelSerializer

from account.models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model: UserModel = UserModel
        exclude: List[str] = ['password', 'is_active', 'is_admin', 
            'is_superuser', 'last_login', 'user_permissions', 'groups']
