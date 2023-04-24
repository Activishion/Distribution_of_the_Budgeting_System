from datetime import datetime, timedelta
from typing import List

from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, ListAPIView,
    RetrieveUpdateAPIView)
from rest_framework.response import Response

from service.models import Message, News, Reporting
from service.serializers import (MessageSerializer, NewsSerializer, 
    ReportSerializer)
from utils.paginator import APIListPaginator


class AllMessageUsers(ListCreateAPIView):
    queryset = Message.objects.filter().reverse()  # за последний год
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
    def list(self, request, pk):
        queryset = Message.objects.get(pk=pk)
        serializer = MessageSerializer(queryset, many=False)
        return Response(
            {'message': serializer.data},
            status=status.HTTP_200_OK
        )


class NewsCreateView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request) -> List[News]:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {'news': serializer.data},
            status=status.HTTP_200_OK
        )

    def create(self, request) -> News:
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {'error': 'Данные не валидны.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(
            {'newNews': serializer.data},
            status=status.HTTP_201_CREATED
        )


class NewsUpdateView(RetrieveUpdateAPIView):
    def get_queryset(self, pk: int):
        return News.objects.get(pk=pk)

    def get_serializer_class(self, **kwargs):
        return NewsSerializer

    def list(self, request, pk: int) -> News:
        queryset = self.get_queryset(pk)
        serializer = self.get_serializer_class(queryset, many=False)
        return Response(
            {'new': serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, pk: int) -> News:
        try:
            instance = self.get_queryset(pk)
        except:
            return Response(
                {'error': 'Объект не найден.'}, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer_class(data=request.data, instance=instance)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {'error': 'Данные не валидны.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(
            {'new': serializer.data},
            status=status.HTTP_200_OK
        )


class ReportCreateView(ListCreateAPIView):
    queryset = Reporting.objects.all()
    serializer_class = ReportSerializer

    def list(self, request) -> List[Reporting]:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {'reports': serializer.data},
            status=status.HTTP_200_OK
        )

    def create(self, request) -> Reporting:
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {'error': 'Данные не валидны.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(
            {'newReport': serializer.data},
            status=status.HTTP_201_CREATED
        )


class ReportUpdateView(RetrieveUpdateAPIView):
    def get_queryset(self, pk: int):
        return Reporting.objects.get(pk=pk)

    def get_serializer_class(self, **kwargs):
        return ReportSerializer

    def list(self, request, pk: int) -> Reporting:
        queryset = self.get_queryset(pk)
        serializer = self.get_serializer_class(queryset, many=False)
        return Response(
            {'report': serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, pk: int) -> Reporting:
        try:
            instance = self.get_queryset(pk)
        except:
            return Response(
                {'error': 'Объект не найден.'}, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer_class(data=request.data, instance=instance)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {'error': 'Данные не валидны.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(
            {'report': serializer.data},
            status=status.HTTP_200_OK
        )
