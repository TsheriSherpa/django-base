from statistics import mode
from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(verbose_name="App Name", max_length=255)
    username = models.CharField(verbose_name="App Username", max_length=255, unique="true")
    password = models.CharField(verbose_name="App Password", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
