from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("TEACHER", "Teacher"),
        ("STUDENT", "Student"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="STUDENT")
    age = models.IntegerField(default=0)
    


