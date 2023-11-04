from django.urls import path
from .views import (ClassListView, ClassDetailVIew, SubjectListView, SubjectDetailView,
                    ResultListView, ResultDetailView)

urlpatterns = [
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/<str:pk>', ClassDetailVIew.as_view(), name='class-detail'),
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<str:pk>', SubjectDetailView.as_view(), name='subject-detail'),
    path('results/', ResultListView.as_view(), name='result-list'),
    path('results/<str:pk>/', ResultDetailView.as_view(), name='result-detail'),
]
