import django
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',tasks,name='tasks'),
    path('task-create/',createTask,name='task-create'),
    path('task-update/<int:pk>/',UpdateTask,name='task-update'),
    path('task-delete/<int:pk>/',DeleteTask,name='task-delete'),
    path('task-complete/<int:pk>/',CompleteTasks,name='task-complete'),
    path('signup/',signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('settings',settings,name='settings')
]
