from django.contrib import admin
from .models import AdminRegister
# Register your models here.


@admin.register(AdminRegister)
class AdminRegisterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'active']
