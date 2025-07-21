from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField("Email address", null=False)
    message = models.TextField(max_length=500)


class ContactInfo(models.Model):
    phone_info = models.CharField("Phone number", max_length=10, null=False)
    email_info = models.EmailField("Email address", null=False)
