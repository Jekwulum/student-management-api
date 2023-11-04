# urls.py
from django.urls import path
from .views import TeacherListView, TeacherDetailView

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<str:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
]
