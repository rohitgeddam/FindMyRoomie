# accounts/urls.py
from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("findpeople/", views.findpeople, name="findpeople"),
    path("myroom/", views.myroom, name="myroom"),
    path("logout/", views.user_logout, name="user_logout"),
    path("", views.home, name="home"),
]
