from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/registr/', views.registr, name='registr'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/appointments/add_appointment/', views.add_appointment, name='appointment'),
    path('accounts/doctors/doctor_list/', views.doctor_list, name='doctors')
]