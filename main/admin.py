from django.contrib import admin
from .models import TodoList

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    search_fields = ['name', 'purpose']
    list_display = ['name', 'purpose']  