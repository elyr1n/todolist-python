from django import forms
from .models import TodoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['name', 'purpose']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '32'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '32'}),
        }