from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_doctor)
