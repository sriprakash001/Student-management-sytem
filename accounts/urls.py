from django.urls import path
from .views import *

urlpatterns = [
    path('sigup/',signup,name='sign-up'),
    path('',login_page , name = '/'),
    path('logout/',logout_page , name='logout'),
]