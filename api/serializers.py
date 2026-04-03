from rest_framework import serializers
from students.models import *
from courses.models import *

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class Course_serializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Attendence_serializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.name",read_only = True)
    course_name = serializers.CharField(source="course.name",read_only = True)
    class Meta:
        model = Attendence
        fields = '__all__'