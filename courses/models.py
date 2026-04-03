from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=70)
    code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name
