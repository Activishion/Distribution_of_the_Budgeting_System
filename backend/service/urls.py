from django.urls import path

from service.views import (AllMessageUsers, MessageUsersById, NewsCreateView,
    NewsIdView, ReportCreateView, ReportIdView)


urlpatterns = [
    path('messages/', AllMessageUsers.as_view()),
    path('messages/<int:pk>/', MessageUsersById.as_view()),
    path('news/', NewsCreateView.as_view()),
    path('news/<int:pk>/', NewsIdView.as_view()),
    path('report/', ReportCreateView.as_view()),
    path('report/<int:pk>/', ReportIdView.as_view()),
]
