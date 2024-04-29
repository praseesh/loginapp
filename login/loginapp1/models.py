from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=20 , null=True, ) 
