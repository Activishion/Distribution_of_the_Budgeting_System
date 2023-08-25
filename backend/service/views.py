from datetime import datetime, timedelta
from typing import List

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import UserModel
from service.models import Message, News, Reporting
from service.pagination import APIPagination
from service.serializers import (MessageSerializer, GetNewsSerializer,
    GetReportSerializer, PostReportSerializer, PostNewsSerializer)


class AllMessageUsers(ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = APIPagination

    @staticmethod
    def time_delta():
        today = datetime.now()
        year_back = timedelta(weeks=52)
        return today-year_back

    def get(self, request):
        data = self.time_delta()
        queryset = Message.objects.filter(date__gt=data)
        serializer = self.get_serializer(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'status': status.HTTP_200_OK,
                'message': serializer.data
            })

        return Response({
            'status': status.HTTP_200_OK,
            'message': serializer.data
        })


class MessageUsersById(ListAPIView):
    def get(self, request, pk):
        queryset = Message.objects.get(pk=pk)
        serializer = MessageSerializer(queryset, many=False)
        return Response({
            'status': status.HTTP_200_OK,
            'message': serializer.data
        })


class UpdateSubscriptionForNews(ListCreateAPIView):
    def get(self, request) -> List[News]:
        queryset = News.objects.all()
        serializer = GetNewsSerializer(queryset, many=True)
        
        return Response({
            'status': status.HTTP_200_OK,
            'news': serializer.data
        })

    def post(self, request) -> News:
        serializer = PostNewsSerializer(data=request.data)
        subscription_check = UserModel.objects.get(email=request.data['user'])

        if str(subscription_check.news_subscription) == request.data['subscription']:
            return Response({
                'status': 'Status has not changed'
            })
        subscription_check.news_subscription = request.data['subscription']   
        subscription_check.save()

        serializer.is_valid(raise_exception=False)
        serializer.save()

        return Response({
            'status': status.HTTP_201_CREATED,
            'newNews': serializer.data
        })


class NewsCreateView(CreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostNewsSerializer
        elif self.request.method == 'GET':
            return GetNewsSerializer

    def post(self, request) -> News:
        serializer = PostNewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'newNews': serializer.data
        })


class ReportCreateView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostReportSerializer
        elif self.request.method == 'GET':
            return GetReportSerializer
        
    def get_queryset(self):
        return Reporting.objects.all()

    def get(self, request) -> List[Reporting]:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'status': status.HTTP_200_OK,
                'reports': serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': status.HTTP_200_OK,
            'reports': serializer.data
        })

    def post(self, request) -> Reporting:
        serializer = PostReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': status.HTTP_201_CREATED,
            'newReport': serializer.data
        })


class ReportIdView(APIView):
    def get(self, request, pk):
        queryset = Reporting.objects.get(pk=pk)
        serializer = GetReportSerializer(queryset, many=False)
        return Response({
            'status': status.HTTP_200_OK,
            'report': serializer.data
        })
