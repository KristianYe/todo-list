from django.urls import path

from todo_app.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_app"
