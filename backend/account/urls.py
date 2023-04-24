from django.urls import path

from account.views import UsersListView


urlpatterns = [
    path('', UsersListView.as_view()),
]
