from django.db import models


class SignUp(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# Create your models here.
