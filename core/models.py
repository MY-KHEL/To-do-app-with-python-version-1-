from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=True , null= True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['complete']