from django.urls import path
from .views import (UserListAV, UserDetailView, LoginAPIView)

urlpatterns = [
    path('users/', UserListAV.as_view(), name='user-list'),
    path('users/<str:email>', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginAPIView.as_view(), name='login')
]
