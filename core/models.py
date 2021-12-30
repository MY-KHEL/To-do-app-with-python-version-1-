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

class Theme(models.Model):
    COLORS=(
        ('red','red'),
        ('pink','pink'),
        ('lightpink','light pink'),
        ('lightgreen','light green'),
        ('orange','orange'),
        ('yellow','yellow'),
        ('lightgoldenrodyellow','light yellow'),
        ('green','green'),
        ('blue','blue'),
        ('lightblue','light blue'),
        ('Indigo','indigo'),
        ('white','white'),
        ('black','black'),
        

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    background_color = models.CharField(max_length = 150,choices=COLORS)
    text_color = models.CharField(max_length = 150,choices=COLORS)
    