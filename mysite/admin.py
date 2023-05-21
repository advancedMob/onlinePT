from django.contrib import admin
from .models import User, Trainer, Post, Reply

# Register your models here.
admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Post)
admin.site.register(Reply)