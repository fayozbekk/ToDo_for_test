from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('api/v1/tasks/create/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/v1/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]