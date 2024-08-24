from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'password1', 'password2')
        widgets = {
            'avatar': forms.FileInput()
        }
