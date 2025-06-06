from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginUserForm, RegisterUserForm, ArticlesForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import Articles
from datetime import datetime

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/test.html')


def reg(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/questions')
    else:
        form = RegisterUserForm()
    return render(request, 'main/registration.html', {'form': form})


def login1(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/questions/')
    else:
        form = LoginUserForm()
    return render(request, 'main/login.html', {'form': form})


def questions(request):
    return render(request, 'main/questions.html')


def new_question(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        print(form)
        if form.is_valid():
            print(1)
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.date = datetime.now()
            obj.anons = obj.full_text[:50]
            obj.save()
            return redirect('/questions/')
        else:
            error = 'Форма заполнена неверно'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/new_question.html', data)


def user_logout(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'main/profile.html')
