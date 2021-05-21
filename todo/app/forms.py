from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        labels = {
            'complete': 'Check if Completed'
        }
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add new task...'})

        }

