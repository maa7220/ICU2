from rest_framework import generics, status, views
from rest_framework.response import Response
from .serializer import AddAdminSerializer
from .models import AdminRegister
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .serializer import SendEmailSerializer


# Create your views here.
class AdminRegisterView(generics.ListCreateAPIView):
    serializer_class = AddAdminSerializer
    queryset = AdminRegister.objects.all()


link = 'http://127.0.0.1:8000/api/signup_admin'


class sendEmail(views.APIView):
    serializer_class = SendEmailSerializer

    def post(self, request, id=None):
        data = request.data
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data.get('recipient_list'),]

        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            email = EmailMessage(
                "Hi From ICU", f"Your account accept go to this link to create your account || {link} ||", email_from, recipient_list)
            email.send()
            return Response({"message": "Email Send "})
        else:
            return Response(serializer.errors)
