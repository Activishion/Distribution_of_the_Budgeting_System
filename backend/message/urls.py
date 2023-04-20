from django.urls import path

from message.views import AllMessageUsers, MessageUsersById


urlpatterns = [
    path('', AllMessageUsers.as_view()),
    path('<int:pk>/', MessageUsersById.as_view()),
]
