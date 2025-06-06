from . import views
from django.urls import path
from .views import NewsDetailView


urlpatterns = [
    path('', views.questions, name='questions'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail')
]