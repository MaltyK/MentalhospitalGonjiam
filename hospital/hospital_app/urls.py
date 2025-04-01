from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, ServiceViewSet, AppointmentViewSet, DiagnoseViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'diagnoses', DiagnoseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]