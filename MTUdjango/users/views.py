from django.shortcuts import render


def user(request):
    return render(request, 'main/index.html')


def reg(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')