from typing import List

from rest_framework.generics import ListAPIView

from account.serializers import UserSerializer
from utils.paginator import APIListPaginator


class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    pagination_class = APIListPaginator
