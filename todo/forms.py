from django import forms
from .models import Task


class TaskFormFast(forms.Form):
    model = Task
    template_name = "todo/new_task_fast.html"
    text = forms.CharField(max_length=40)
