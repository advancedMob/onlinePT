from django.contrib import admin
from .models import User, Trainer, Board, ReplyUser, ReplyTrainer

# Register your models here.
admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Board)
admin.site.register(ReplyUser)
admin.site.register(ReplyTrainer)
