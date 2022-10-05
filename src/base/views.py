from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

from .filters import ProfileFilter


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    return render(request, "index.html")


@login_required()
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

    person = Profile.objects.all()
    form = ProfileForm()
    return render(request, "pages/profile.html", {"form": form, "profiles": person})


@login_required()
def findpeople(request):
    qs = Profile.objects.filter(visibility=True)
    f = ProfileFilter(request.GET, queryset=qs)
    return render(request, "pages/findpeople.html", {"filter": f})


@login_required()
def myroom(request):
    return render(request, "pages/myroom.html")


def user_logout(request):
    logout(request)
    messages.error(request, "Logged out successfully!")
    return redirect("home")
