from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/test.html')


def reg(request):
    return render(request, 'main/registration.html')


def login(request):
    return render(request, 'main/login.html')
