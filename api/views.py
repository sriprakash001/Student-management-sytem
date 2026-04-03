from rest_framework import generics
from students.models import Student,Attendence
from students.models import Course
from .serializers import *
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permission import *


# Student API's
class Student_view(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id','name']
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]   #only admin can create student
        return [IsAuthenticated()]
    
class Student_viewById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]  # only admin can update/delete
        return [IsAuthenticated()]  # everyone can view
    
# Course API's
class Course_view(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = Course_serializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id','name']
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]  # only admin can create course
        return [IsAuthenticated()]  # everyone can view

class Course_viewById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = Course_serializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]  # only admin can update/delete
        return [IsAuthenticated()]  # everyone can view

# Attendence API's
class Attendence_view(generics.ListCreateAPIView):
    queryset = Attendence.objects.all()
    serializer_class = Attendence_serializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["student__name", "course__name", "status"]
    ordering_fields = ["date", "id", "status"]
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsTeacherOrAdmin()]  # admin or teacher can mark attendance
        return [IsAuthenticated()]  # everyone can view

class Attendence_viewById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendence.objects.all()
    serializer_class = Attendence_serializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsTeacherOrAdmin()]  # teacher/admin can edit attendance
        return [IsAuthenticated()]  # everyone can view
