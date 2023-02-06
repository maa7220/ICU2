from django.urls import path
from .views import AdminRegisterView, sendEmail
urlpatterns = [
    path('register', AdminRegisterView.as_view(), name='register_admins'),
    path('send_email/<int:id>', sendEmail.as_view(), name='send_email'),
]
