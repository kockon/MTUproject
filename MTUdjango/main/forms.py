from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from .models import Articles



class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Почта')

    class Meta:
        model = User
        fields = ['username', 'email']


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Введите заголовок",
                'maxlength': "150",
            }),
            "full_text": Textarea(attrs={
                'placeholder': "Опишите свой вопрос подробно"
            }),
        }

