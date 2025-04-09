from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from . import models
from . import forms

# Create your views here.

def home(request):
    return render(request, 'hospital_app/home.html')

def registr(request):
    return render(request, 'hospital_app/registr.html')

# Patient
def patient_list(request):
    patients = models.Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

@login_required
def add_patient(request):
    if request.method == "POST":
        form = forms.PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = forms.PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(models.Patient, pk=pk)
    if request.method == "POST":
        form = forms.PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = forms.PatientForm(instance=patient)
    return render(request, 'patients/edit_patient.html', {'form': form})

@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(models.Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/delete_patient.html', {'patient': patient})

# Doctor
def doctor_list(request):
    doctors = models.Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

@login_required
def add_doctor(request):
    if request.method == "POST":
        form = forms.DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = forms.DoctorForm()
    return render(request, 'doctors/add_doctor.html', {'form': form})

@login_required
def edit_doctor(request, pk):
    doctor = get_object_or_404(models.Doctor, pk=pk)
    if request.method == "POST":
        form = forms.DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = forms.DoctorForm(instance=doctor)
    return render(request, 'doctors/edit_doctor.html', {'form': form})

@login_required
def delete_doctor(request, pk):
    doctor = get_object_or_404(models.Doctor, pk=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/delete_doctor.html', {'doctor': doctor})

# Service
def service_list(request):
    services = models.Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def add_service(request):
    if request.method == "POST":
        form = forms.ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = forms.ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})

@login_required
def edit_service(request, pk):
    service = get_object_or_404(models.Service, pk=pk)
    if request.method == "POST":
        form = forms.ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = forms.ServiceForm(instance=service)
    return render(request, 'services/edit_service.html', {'form': form})

@login_required
def delete_service(request, pk):
    service = get_object_or_404(models.Service, pk=pk)
    if request.method == "POST":
        service.delete()
        return redirect('service_list')
    return render(request, 'services/delete_service.html', {'service': service})

# Appointment
def appointments_list(request):
    appointments = models.Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def add_appointment(request):
    if request.method == "POST":
        form = forms.AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = forms.AppointmentForm()
    return render(request, 'appointments/add_appointment.html', {'form': form})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(models.Appointment, pk=pk)
    if request.method == "POST":
        form = forms.AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = forms.AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form})

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(models.Appointment, pk=pk)
    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})

# Diagnose
def diagnose_list(request):
    diagnoses = models.Diagnose.objects.all()
    return render(request, 'diagnoses/diagnose_list.html', {'diagnoses': diagnoses})

@login_required
def add_diagnose(request):
    if request.method == "POST":
        form = forms.DiagnoseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnose_list')
    else:
        form = forms.DiagnoseForm()
    return render(request, 'diagnoses/add_diagnose.html', {'form': form})

@login_required
def edit_diagnose(request, pk):
    diagnose = get_object_or_404(models.Diagnose, pk=pk)
    if request.method == "POST":
        form = forms.DiagnoseForm(request.POST, instance=diagnose)
        if form.is_valid():
            form.save()
            return redirect('diagnose_list')
    else:
        form = forms.DiagnoseForm(instance=diagnose)
    return render(request, 'diagnoses/edit_diagnose.html', {'form': form})

@login_required
def delete_diagnose(request, pk):
    diagnose = get_object_or_404(models.Diagnose, pk=pk)
    if request.method == "POST":
        diagnose.delete()
        return redirect('diagnose_list')
    return render(request, 'diagnoses/delete_diagnose.html', {'diagnose': diagnose})

# Payment
def payment_list(request):
    payments = models.Payment.objects.all()
    return render(request, 'payments/payment_list.html', {'payments': payments})

@login_required
def add_payment(request):
    if request.method == "POST":
        form = forms.PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = forms.PaymentForm()
    return render(request, 'payments/add_payment.html', {'form': form})

@login_required
def edit_payment(request, pk):
    payment = get_object_or_404(models.Payment, pk=pk)
    if request.method == "POST":
        form = forms.PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = forms.PaymentForm(instance=payment)
    return render(request, 'payments/edit_payment.html', {'form': form})

@login_required
def delete_payment(request, pk):
    payment = get_object_or_404(models.Payment, pk=pk)
    if request.method == "POST":
        payment.delete()
        return redirect('payment_list')
    return render(request, 'payments/delete_payment.html', {'payment': payment})

# Registration view.
def registr(request):
    if request.method == "POST":
        form = forms.RegistrForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = forms.RegistrForm()
    return render(request, 'hospital_app/registr.html', {'form': form})
