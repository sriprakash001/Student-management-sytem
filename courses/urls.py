from django.urls import path
from .views import *

urlpatterns = [
    path('create/',course_create,name = 'course_create'),
    path('list',course_list,name = 'courses_list'),
    path('update/<int:pk>/',course_update,name = 'course_update'),
    path('delete/<int:pk>/',course_delete,name = 'course_delete')
]