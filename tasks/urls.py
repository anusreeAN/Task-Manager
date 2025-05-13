from django.urls import path
from .views import TaskCreateView, TaskListView, TaskRetrieveView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),  
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<str:task_id>/', TaskRetrieveView.as_view(), name='task-retrieve'), 
    path('tasks/<str:task_id>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<str:task_id>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
