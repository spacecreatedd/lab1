from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Авторизация, вход и выход
class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(help_text="", label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(help_text="", label="Подтвердите пароль", widget=forms.PasswordInput)
    username = forms.CharField(help_text="", label="Логин")
    email = forms.CharField(help_text="", label="Электронная почта")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
        # widgets = {
        #     "username": forms.CharField(attrs={
        #         "class": "qwe"
        #     })
        # }


