from django.urls import path

from .views import TodoListView, TodoDetailView, UserListView, UserDetailView


urlpatterns = [
    path('todos', TodoListView.as_view()),
    path('todos/<int:pk>', TodoDetailView.as_view()),
    path('users', UserListView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
]