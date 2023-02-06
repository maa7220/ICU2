from django.contrib import admin
from .models import Medicine, Medicines
# Register your models here.


# =========== Medicines ==============
@admin.register(Medicines)
class Medicines(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 25


# =========== Medicine ==============
@admin.register(Medicine)
class Medicine(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'dosage', 'doctor', 'patient']
    list_per_page = 10
