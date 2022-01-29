from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=5, default="43701",
        validators=[RegexValidator(
             regex=r'^\d{5}$',
             message='Must be valid zipcode in formats from 00000 to 99999',
             )],)
    phone = models.CharField(max_length=15, default="+91 (123) 456-7890",
        validators=[RegexValidator(
            regex=r'/^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$/gm',
            message='Must include the country code with the plus sign followed by your phone number.'
            )],)
