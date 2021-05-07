from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    
    if request.method == 'POST':
	    form = TodoForm(request.POST) 
	    if form.is_valid():
		    form.save()	
	    return redirect('/') 

    context = {'todos':todos, 'form':form}
    return render(request, 'todo/todo.html',context)

def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    context = {'form':form}
    if request.method=='POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'todo/update_todo.html',context)

def deleteTodo(request, pk):
    item = Todo.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'todo/delete.html', context)

