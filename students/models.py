from django.db import models
from courses.models import Course
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"

class Attendence(models.Model):
    STATUS_CHOICES = [
        ("Present","Present"),
        ("Absent","Absent"),
        ("Late","Late"),
        ("Excused","Excused")
    ]
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student','course','date')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student.name}-{self.course.name}-{self.date}-{self.status}"