from django.urls import path

from service.views import (AllMessageUsers, MessageUsersById,
    ReportCreateView, ReportIdView, NewsCreateView)


urlpatterns = [
    path('messages', AllMessageUsers.as_view()),
    path('messages/<int:pk>', MessageUsersById.as_view()),
    path('news', NewsCreateView.as_view()),
    path('report', ReportCreateView.as_view()),
    path('report/<int:pk>', ReportIdView.as_view()),
]
