from django.db import models
from django.http.response import HttpResponsePermanentRedirect

# Create your models here.
class Mall(models.Model):
    product = models.CharField(max_length=30)
    price = models.CharField(max_length=30) 
    description = models.TextField()