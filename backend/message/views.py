from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response

from message.models import Message
from message.serializers import MessageSerializer
from utils.paginator import APIListPaginator


class AllMessageUsers(ListCreateAPIView):
    queryset = Message.objects.filter().reverse()
    serializer_class = MessageSerializer
    pagination_class = APIListPaginator

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {'message': serializer.data},
            status=status.HTTP_200_OK
        )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'newMessage': serializer.data},
            status=status.HTTP_201_CREATED
        )


class MessageUsersById(ListAPIView):
    serializer_class = MessageSerializer

    def list(self, request, pk):
        queryset = Message.objects.get(pk=pk)
        serializer = self.get_serializer(queryset, many=False)
        return Response(
            {'message': serializer.data},
            status=status.HTTP_200_OK
        )
