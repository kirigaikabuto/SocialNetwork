from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register_page, name="register_page"),
]

