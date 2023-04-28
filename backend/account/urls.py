from django.urls import path

from account.views import UserView


urlpatterns = [
    path('<int:pk>/', UserView.as_view()),
]
