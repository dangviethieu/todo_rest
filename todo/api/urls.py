from django.urls import path

from .views import TodoListView, TodoDetailView


urlpatterns = [
    path('todos', TodoListView.as_view()),
    path('todos/<int:todo_id>', TodoDetailView.as_view()),
]