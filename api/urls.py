from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("students/",Student_view.as_view(), name="api_students"),
    path("students/<int:pk>/",Student_viewById.as_view(), name="api_student_detail"),

    # COURSES
    path("courses/",Course_view.as_view(), name="api_courses"),
    path("courses/<int:pk>/",Course_viewById.as_view(), name="api_course_detail"),
    
    # ATTTENDENCE
    path("attendence/",Attendence_view.as_view(),name="api_attendence"),
    path("attendence/<int:pk>/",Attendence_viewById.as_view(),name="api_attendence_detail"),

    #JWT
    path("token/",TokenObtainPairView.as_view(),name = "token_obtain"),
    path("token/refresh/",TokenRefreshView.as_view(),name = "token_refersh"),
]