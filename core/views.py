from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm, TaskForm
from django.contrib.auth.models import User
from .models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

@login_required
def tasks(request):
    user = request.user
    #print(user)
    tasks = Tasks.objects.filter(user=user)
    
       
    context={
        'tasks':tasks
    }
    return render(request,'index.html',context)

def createTask(request):
    user = request.user
    form = TaskForm(request.POST or None)
    if request.method=='POST':
        form = TaskForm(request.POST,initial={'user':user})
        if form.is_valid:
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(initial={'user':user})

    context={
        'form':form
    }
    return render(request,'tasks_create.html',context)

def UpdateTask(request,pk):
    item =  Tasks.objects.get(id=pk)
    form = TaskForm(request.POST or None)
    if request.method=='POST':
        form = TaskForm(request.POST,instance=item)
        if form.is_valid:
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=item)

    context={
        'form':form
    }
    return render(request,'tasks_update.html',context)

def DeleteTask(request,pk):
    item = Tasks.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('tasks')
    context={
        'item':item
    }
    return render(request,'tasks_delete.html',context)

def CompleteTasks(request,pk):
    item = Tasks.objects.get(id=pk)
    if request.method=='POST':
        item.complete = True
        item.save()
        return redirect('tasks')
    context={
        'item':item
    }
    return render(request,'tasks_complete.html',context)

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('tasks')
    else:
        form = SignUpForm()
    context={
        'form':form
    }
    return render(request,'registration/signup.html',context)