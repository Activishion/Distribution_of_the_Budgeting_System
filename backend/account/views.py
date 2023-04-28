from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import UserModel
from account.serializers import UserSerializer


class UserView(APIView):
    def get(self, request, pk):
        queryset = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(queryset, many=False)
        return Response(
            {'user': serializer.data},
            status=status.HTTP_200_OK
        )
