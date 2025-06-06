from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from main.models import Answers


class AnswersForm(ModelForm):
    class Meta:
        model = Answers
        fields = ['answer']

        widgets = {
            "answer": Textarea(attrs={
                'placeholder': "Опишите свой вопрос подробно"
            }),
        }
