from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm, TaskForm, Settings
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

@login_required
def tasks(request):
    user = request.user
    theme = Theme.objects.filter(user=user)
    for x in theme:
        print(x.background_color)
        theme=x
    tasks = Tasks.objects.filter(user=user)
    
    context={
        'tasks':tasks,
        'theme':theme,
    }
    return render(request,'index.html',context)

    return render(request,'base.html',context)

def createTask(request):
    user = request.user
    theme = Theme.objects.filter(user=user)
    form = TaskForm(request.POST or None)
    for x in theme:
        print(x.background_color)
        theme=x
    if request.method=='POST':
        form = TaskForm(request.POST,initial={'user':user})
        if form.is_valid:
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(initial={'user':user})

    context={
        'theme':theme,
        'form':form
    }
    return render(request,'tasks_create.html',context)

def UpdateTask(request,pk):
    item =  Tasks.objects.get(id=pk)
    user = request.user
    theme = Theme.objects.filter(user=user)
    form = TaskForm(request.POST or None)
    for x in theme:
        print(x.background_color)
        theme=x
    if request.method=='POST':
        form = TaskForm(request.POST,instance=item)
        if form.is_valid:
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=item)

    context={
        'theme':theme,
        'form':form
    }
    return render(request,'tasks_update.html',context)

def DeleteTask(request,pk):
    user = request.user
    theme = Theme.objects.filter(user=user)
    item = Tasks.objects.get(id=pk)
    for x in theme:
        print(x.background_color)
        theme=x
    if request.method=='POST':
        item.delete()
        return redirect('tasks')
    context={
        'theme':theme,
        'item':item
    }
    return render(request,'tasks_delete.html',context)

def CompleteTasks(request,pk):
    user = request.user
    theme = Theme.objects.filter(user=user)
    item = Tasks.objects.get(id=pk)
    for x in theme:
        print(x.background_color)
        theme=x 
    if request.method=='POST':
        item.complete = True
        item.save()
        return redirect('tasks')
    context={
        'theme':theme,
        'item':item
    }
    return render(request,'tasks_complete.html',context)

def signup(request):
    user = request.user
    
    form = SignUpForm(request.POST or None)
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            assign = Theme.objects.create(user=user,background_color='white')
            login(request,user)
            return redirect('tasks')
    else:
        form = SignUpForm()
    context={
        
        'form':form
    }
    return render(request,'registration/signup.html',context)

def settings(request):
    user = request.user
    form = Settings(request.POST or None)
    if request.method=='POST':
        form = Settings(request.POST,initial={'user':user})
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = Settings(initial={'user':user})
    context={
        
        'form':form
    }
    return render(request,'settings.html',context)