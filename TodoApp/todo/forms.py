from django import forms
from django.forms import ModelForm
from .models import *

class TodoForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = Todo #which model for form
        fields = '__all__' #which fields allowed in form
