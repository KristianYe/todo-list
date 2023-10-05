from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "datetime_deadline", "tags"]
    success_url = reverse_lazy("todo_app:task-list")

    def form_valid(self, form):
        form.instance.is_done = False
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "datetime_deadline", "tags"]
    success_url = reverse_lazy("todo_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


