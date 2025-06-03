from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Почта')

    class Meta:
        model = User
        fields = ['username', 'email']


    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if get_user_model().objects.filter(email=email).exists():
    #         raise forms.ValidationError('Почта привязана к другому аккаунту')

