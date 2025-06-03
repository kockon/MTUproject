from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/test.html')


def reg(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        print(form.data)
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
        print(1)
        if form.is_valid():
            print(2)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('questions/')
    else:
        form = LoginUserForm()
    return render(request, 'main/login.html', {'form': form})


def questions(request):
    return render(request, 'main/questions.html')

def user_logout(request):
    logout(request)
    return redirect('/')
