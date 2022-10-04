# accounts/urls.py
from django.urls import path

from .views import SignUpView,  myprofile


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("myprofile/", myprofile, name="myprofile" )
]