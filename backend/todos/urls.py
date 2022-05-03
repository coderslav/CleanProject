from django.urls import path
from .views import ListTodoAPIView, DetailTodoAPIView

urlpatterns = [
    path('api/', ListTodoAPIView.as_view(), name='todo_list'),
    path('api/<int:pk>', DetailTodoAPIView.as_view(), name='todo_detail')
]
