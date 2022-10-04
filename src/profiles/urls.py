# accounts/urls.py
from django.urls import path

from .views import SignUpView, findpeople


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("findpeople/", findpeople, name="findpeople"),
]