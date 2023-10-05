from django import forms

from todo_app.models import Task


class TaskForm(forms.ModelForm):
    datetime_deadline = forms.DateTimeField(
        required=False,
        widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local"}),
        label="Deadline"
    )

    class Meta:
        model = Task
        fields = ("content", "tags", "datetime_deadline")
