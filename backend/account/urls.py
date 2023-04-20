from django.urls import path

from account.views import (UsersListView, NewsCreateView, NewsUpdateView,
    ReportCreateView, ReportUpdateView)


urlpatterns = [
    path('', UsersListView.as_view()),
    path('news/', NewsCreateView.as_view()),
    path('news/<int:pk>/', NewsUpdateView.as_view()),
    path('report/', ReportCreateView.as_view()),
    path('report/<int:pk>/', ReportUpdateView.as_view()),
]
