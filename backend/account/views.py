from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from account.models import UserModel
from account.serializers import SubscriptionСheck


class UserView(CreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubscriptionСheck
        
    def post(self, request):
        """ Checking the status of a news subscription. """
        queryset = get_object_or_404(UserModel, email=request.data['email'])
        return Response({
            'status_subscription': queryset.news_subscription,
        })
