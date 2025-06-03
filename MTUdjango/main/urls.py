from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('register/', views.reg, name='reg'),
    path('login/', views.login1, name='login1'),
    path('questions/', views.questions, name='questions'),
    path('logout/', views.user_logout, name='user_logout')
]