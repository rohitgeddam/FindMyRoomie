from django.shortcuts import render
from .forms import PersonForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def profile(request):
    form = PersonForm()
    return render(request, "profile.html", {"form": form})


def matches(request):
    return render(request, "matches.html")
