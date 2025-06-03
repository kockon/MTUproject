from . import views
from django.urls import path


urlpatterns = [
    path('', views.user, name='news_home'),
    path('register/', views.reg, name='reg'),
    path('login/', views.login, name='login')
]