from django.db import models


class User(models.Model):
    """
    Modle class to keep user related data, we keep minimum no of fields here.
        1. name
        2. data of birth(dob)
        3. email
        4. auth_id(auth service user id)
    """
    Roles = (
        ('AD', 'Admin'),
        ('PA', 'Patient'),
        ('DO', 'Doctor'),
    )

    name = models.CharField(max_length=64, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    role = models.CharField(max_length=2, choices=Roles, default='PA')
    auth_id = models.IntegerField(default=0)
