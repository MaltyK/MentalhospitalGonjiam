from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/registr/', views.registr, name='registr'),
    path('accounts/profile/', views.home, name='profile'),
]