from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=64)
    content=models.TextField()
    due_date=models.DateTimeField()
    creation_date=models.DateTimeField(default=timezone.now())
    done=models.CharField(max_length=32,default='No')
    def get_absolute_url(self):
        return(reverse("show"))
    def show_time_left(self):
        l=timezone.now()-self.due_date
        return str(l)

class done(models.Model):
    title=models.CharField(max_length=64)
