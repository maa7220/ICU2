from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class AdminRegister(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = PhoneNumberField(null=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['active']
