from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoListForm

def home(request):
    todolist = TodoList.objects.all()
    return render(request, 'main/main-page/main-page.html', {'todolist': todolist})

def add_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = TodoListForm()
        
    return render(request, 'main/main-page/add_list.html', {'form': form})

def edit_list(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = TodoListForm(instance=todo)

    return render(request, 'main/main-page/edit_list.html', {'form': form})

def delete_list(request, pk):
    form = get_object_or_404(TodoList, pk=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('main:home')

    return render(request, 'main/main-page/delete_list.html', {'form': form})