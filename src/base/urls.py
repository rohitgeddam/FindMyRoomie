# accounts/urls.py
from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("findpeople/", views.findpeople, name="findpeople"),
    path("logout/", views.user_logout, name="user_logout"),
    path("myroom/", views.myroom, name="myroom"),

]

