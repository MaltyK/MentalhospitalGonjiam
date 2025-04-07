from django import forms
from . import models

class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['fio', 'birthdate', 'gender', 'phone', 'email', 'address', 'oms']
        labels = {
            "fio": "ФИО",
            "birthdate": "Дата рождения",
            "gender": "Пол",
            "phone": "Номер телефона",
            "email": "Эл. Почта",
            "address": "Адрес",
            "oms": "Омс",
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['fio', 'spec', 'cab', 'phone', 'email']
        labels = {
            "fio": "ФИО",
            "spec": "Специальность",
            "cab": "Кабинет",
            "phone": "Номер телефона",
            "email": "Эл. Почта",
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = ['name', 'price', 'description', 'duration']
        labels = {
            "name": "Название",
            "price": "Стоимость",
            "description": "Описание",
            "duration": "Длительность",
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['patient', 'doctor', 'service', 'datetime', 'status']
        labels = {
            "patient": "Пациент",
            "doctor": "Доктор",
            "service": "Услуга",
            "datetime": "Назначенная дата",
            "status": "Статус",
        }

class DiagnoseForm(forms.ModelForm):
    class Meta:
        model = models.Diagnose
        fields = ['appointment']
        labels = {
            "appointment": "Приём",
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ['appointment', 'amount', 'payment_date', 'payment_method']
        labels = {
            "appointment": "Приём",
            "amount": "Сумма",
            "payment_date": "Дата оплаты",
            "payment_method": "Метод оплаты",
        }