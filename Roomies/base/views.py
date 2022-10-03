from django.shortcuts import render
from .forms import PersonForm
from .models import Person


# Create your views here.
def home(request):
    return render(request, "home.html")


def profile(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    person = Person.objects.all()
    form = PersonForm()
    return render(request, "profile.html", {"form": form, "profiles": person})


def matches(request):
    return render(request, "matches.html")
