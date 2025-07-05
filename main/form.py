from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ваше имя"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "forms-control",
            "placeholder": "Оставьте комментарий"
        })
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
