from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Board, Comment, CommentT
from django.forms import TextInput

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 1200px",
                'placeholder': '댓글을 작성해주세요'
            })
        }

class CommentTForm(forms.ModelForm):
    class Meta:
        model = CommentT
        fields = ['comment']
        widgets = {
            'comment': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 1200px",
                'placeholder': '댓글을 작성해주세요'
            })
        }