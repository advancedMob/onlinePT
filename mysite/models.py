from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10)
    useremail = models.EmailField(max_length=120)
    password = models.CharField(max_length=64)
    usertype = 'user'

    def __str__(self):
        return self.username

class Trainer(models.Model):
    username = models.CharField(max_length=10)
    useremail = models.EmailField(max_length=120)
    password = models.CharField(max_length=64)
    usertype = 'trainer'

    def __str__(self):
        return self.username