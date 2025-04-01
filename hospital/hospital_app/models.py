from django.db import models

class Patient(models.Model):
    fio = models.CharField(max_length=255)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    oms = models.CharField(max_length=50)

    def __str__(self):
        return self.fio

class Doctor(models.Model):
    fio = models.CharField(max_length=255)
    spec = models.CharField(max_length=100)
    cab = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.fio

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    datetime = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.datetime}"

class Diagnose(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='diagnoses')
    # Добавьте другие поля для диагноза, если необходимо

    def __str__(self):
        return f"Diagnose for {self.appointment}"
    
class Payment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма платежа
    payment_date = models.DateTimeField(auto_now_add=True)  # Дата оплаты
    payment_method = models.CharField(max_length=50)  # Способ оплаты

    def __str__(self):
        return f"Payment of {self.amount} for {self.appointment} on {self.payment_date}"