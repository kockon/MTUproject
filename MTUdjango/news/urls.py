from . import views
from django.urls import path


urlpatterns = [
    path('', views.news_home, name='news_home'),
]