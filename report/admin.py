from django.contrib import admin
from .models import DoctorReport, NurseReport


# Register your models here.
@admin.register(DoctorReport)
class DoctorReport(admin.ModelAdmin):
    list_display = ['title', 'patient', 'nurse', 'added_by']

    def nurse(self, obj):
        for nurse in obj.nurse.all():
            return (nurse)

    def patient(self, obj):
        return obj.patient.name


# Register your models here.
@admin.register(NurseReport)
class NurseReport(admin.ModelAdmin):
    list_display = ['title', 'patient', 'doctor', 'added_by']

    def doctor(self, obj):
        return obj.user.username

    def patient(self, obj):
        return obj.patient.name
