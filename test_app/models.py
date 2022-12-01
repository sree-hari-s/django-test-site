from django.db import models

class UserInfo(models.Model):
    username= models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password = models.CharField(max_length=30)