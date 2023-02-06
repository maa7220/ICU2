from django.contrib import admin
from .models import Admin, User, Doctor, Nurse, Patient


# =========== User ==============
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role',
                    'is_superuser', 'is_doctor', 'is_nurse']
    list_per_page = 20
    search_fields = ['username', 'role']

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        users = qs.filter(added_by=request.user)
        if request.user.is_superuser:
            return users


# =========== Doctor ==============
@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email']
    list_per_page = 10

    def username(self, obj):
        return (obj.user.username)

    def email(self, obj):
        return (obj.user.email)

    def name(self, obj):
        return (obj.user.name)


# =========== Doctor ==============
@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ['username', 'name', 'email']
    list_per_page = 10

    def username(self, obj):
        return (obj.user.username)

    def email(self, obj):
        return (obj.user.email)

    def name(self, obj):
        return (obj.user.name)


# =========== Nurse ==============
@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email']
    list_per_page = 10

    def username(self, obj):
        return (obj.user.username)

    def email(self, obj):
        return (obj.user.email)

    def name(self, obj):
        return (obj.user.name)


# =========== Patient ==============
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'disease_type', 'gender',
                    'age', 'room_number', 'doctors', 'nurses']
    search_fields = ['name', 'room_number', 'age', 'gender']
    list_per_page = 10

    def doctors(self, obj):
        for doctor in obj.doctor.all():
            return (doctor)

    def nurses(self, obj):
        for nurse in obj.nurse.all():
            return (nurse)
