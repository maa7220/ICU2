from django_filters.rest_framework import FilterSet
from .models import User, Patient


class UsersFilter(FilterSet):

    class Meta:
        model = User
        fields = {
            'role': ['exact'],
            'username': ['exact', 'contains'],
            'email': [],
            'name': ['contains']
        }


class PatientsFilter(FilterSet):

    class Meta:
        model = Patient
        fields = {
            "room_number": [],
            'name': ['contains']
        }
