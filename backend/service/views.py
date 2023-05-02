from datetime import datetime, timedelta
from typing import List

from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, ListAPIView,
    RetrieveUpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from service.models import Message, News, Reporting
from service.serializers import (MessageSerializer, NewsSerializer, 
    ReportSerializer, PostReportSerializer, PostNewsSerializer)
from utils.paginator import APIListPaginator


class AllMessageUsers(ListCreateAPIView):
    queryset = Message.objects.filter()  # за последний год
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
        serializer = PostNewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'newNews': serializer.data},
            status=status.HTTP_201_CREATED
        )


class NewsUpdateView(APIView):
    def get(self, request, pk):
        queryset = News.objects.get(pk=pk)
        serializer = NewsSerializer(queryset, many=False)
        return Response(
            {'news': serializer.data},
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response(
                {'error': 'Объект не найден.'}, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NewsSerializer(data=request.data, instance=instance)
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
        serializer = PostReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'newReport': serializer.data},
            status=status.HTTP_201_CREATED
        )


class ReportUpdateView(APIView):
    def get(self, request, pk):
        queryset = Reporting.objects.get(pk=pk)
        serializer = ReportSerializer(queryset, many=False)
        return Response(
            {'report': serializer.data},
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        try:
            instance = Reporting.objects.get(pk=pk)
        except:
            return Response(
                {'error': 'Объект не найден.'}, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReportSerializer(data=request.data, instance=instance)
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
