# accounts/urls.py
from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
<<<<<<< HEAD
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("findpeople/", views.findpeople, name="findpeople"),
    path("myroom/", views.myroom, name="myroom"),

]

=======
    path("profile/", views.profile, name="profile"),
    path("findpeople/", views.findpeople, name="findpeople"),
    path("myroom/", views.myroom, name="myroom"),
    path("", views.home, name="home"),
]
>>>>>>> 1c74477 (-)
