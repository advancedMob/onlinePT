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

class Board(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=5000, null=True)
    last_updated = models.DateField(auto_now_add=True, null=True)
    writer = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.subject

"""
class ReplyUser(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.message[:20]

class ReplyTrainer(models.Model):
    writer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message[:20]
"""

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Board, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comment'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'

class CommentT(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    post = models.ForeignKey(Board, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'commentT'
        verbose_name = '댓글T'
        verbose_name_plural = '댓글T'

