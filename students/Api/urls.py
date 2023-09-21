from django.urls import path
from .views import (StudentListView, StudentDetailView, student_search, StudentPaginationView)

urlpatterns = [
    path('students/pagination/list/', StudentPaginationView.as_view(), name='student-pagination-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<str:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('students/<str:pk>/search', student_search, name='student-search'),
]
