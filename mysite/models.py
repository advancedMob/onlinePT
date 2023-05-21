from django.db import models
from django_quill.fields import QuillField
from django.shortcuts import render

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

class Post(models.Model):
    message = models.TextField(max_length=5000, null=True)
    subject = models.CharField(max_length=255)
    last_updated = models.DateField(auto_now_add=True, null=True)
    writer = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject

class Reply(models.Model):
    """게시글에 대한 댓글"""
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, related_name='posts', on_delete=models.CASCADE)
    updated_at = models.DateField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.message[:20]

