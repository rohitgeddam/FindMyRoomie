from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import ProfileForm
from .models import Profile


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    return render(request, "index.html")


def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

    person = Profile.objects.all()
    form = ProfileForm()
    return render(request, "pages/profile.html", {"form": form, "profiles": person})


def findpeople(request):
    return render(request, "pages/findpeople.html")


def myroom(request):
    return render(request, "pages/myroom.html")


def user_logout(request):
    logout(request)
    return redirect("home")
