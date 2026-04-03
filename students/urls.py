from django.urls import path
from .views import *

urlpatterns = [
    path('student/create/',student_create,name='student_create'),
    path('student/list/',student_list,name='students_list'),
    path('student/update/<int:pk>/',student_update,name='student_update'),
    path('student/delete/<int:pk>/',student_delete,name='student_delete'),
    path('student/entroll/',entroll_student,name='student_entroll'),
    path('dashboard/',dashboard,name='dashboard'),
    # Attendence
    path('attendence/',mark_attendence,name = 'attendence'),
    path('attendence/dash/',attendance_dashboard,name = "attendence_dash"),

]