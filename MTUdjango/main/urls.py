from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('register/', views.reg, name='reg'),
    path('login/', views.login1, name='login1'),
    path('logout/', views.user_logout, name='user_logout'),
    path('new_question/', views.new_question, name='new_question'),
    path('profile/', views.profile, name='profile')
]