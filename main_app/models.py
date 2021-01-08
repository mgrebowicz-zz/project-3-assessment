from django.db import models
from django.urls import reverse

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('index')