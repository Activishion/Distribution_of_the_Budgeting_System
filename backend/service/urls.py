from django.urls import path

from service.views import (AllMessageUsers, MessageUsersById, NewsCreateView,
    NewsUpdateView, ReportCreateView, ReportUpdateView)


urlpatterns = [
    path('', AllMessageUsers.as_view()),
    path('<int:pk>/', MessageUsersById.as_view()),
    path('news/', NewsCreateView.as_view()),
    path('news/<int:pk>/', NewsUpdateView.as_view()),
    path('report/', ReportCreateView.as_view()),
    path('report/<int:pk>/', ReportUpdateView.as_view()),
]