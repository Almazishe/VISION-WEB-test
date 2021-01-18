from django.urls import path

from .views import UserAccountListAPIView


urlpatterns = [
    path('users/list/', UserAccountListAPIView.as_view()),
]