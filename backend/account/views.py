from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from account.models import News, Reporting
from account.serializers import UserSerializer, NewsSerializer, ReportSerializer
from utils.paginator import APIListPaginator


class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    pagination_class = APIListPaginator


class NewsCreateView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {'news': serializer.data},
            status=status.HTTP_200_OK
        )

    def create(self, request):
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

    def list(self, request, pk: int):
        queryset = self.get_queryset(pk)
        serializer = self.get_serializer_class(queryset, many=False)
        return Response(
            {'new': serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, pk: int):
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

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {'reports': serializer.data},
            status=status.HTTP_200_OK
        )

    def create(self, request):
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

    def list(self, request, pk: int):
        queryset = self.get_queryset(pk)
        serializer = self.get_serializer_class(queryset, many=False)
        return Response(
            {'report': serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, pk: int):
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
