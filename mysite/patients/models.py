from django.db import models


class Patient(models.Model):

    patientuid = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    dob = models.DateField('date of birth')
    phone = models.CharField(max_length=15)
    email  = models.CharField(max_length=100)
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)

