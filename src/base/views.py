from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SignUpForm
from .models import Profile

# from django.contrib.auth.forms import UserCreationForm

from .filters import ProfileFilter
from .matching import matchings


class SignUpView(generic.CreateView):
    """Sign up View"""

    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    """Render Home Page"""
    return render(request, "index.html")


@login_required()
def profile(request):
    """Render profile page"""
    profile = Profile.objects.get(user=request.user)

    return render(request, "pages/profile.html", {"profile": profile})


@login_required()
def profile_edit(request):
    """Render Edit Profile Page"""
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            p = form.save(commit=False)
            p.is_profile_complete = True
            p.save()

            return redirect("profile")

    person = Profile.objects.all()
    form = ProfileForm(instance=profile)
    return render(
        request, "pages/profile_edit.html", {"form": form, "profiles": person}
    )


@login_required()
def findpeople(request):
    """Render findpeople page"""
    qs = Profile.objects.filter(visibility=True)
    f = ProfileFilter(request.GET, queryset=qs)
    return render(request, "pages/findpeople.html", {"filter": f})


@login_required()
def myroom(request):
    """Render Myroom page based on Profile Completion"""
    if not request.user.profile.is_profile_complete:
        messages.error(request, "Please complete your profile first!")
        return redirect("profile_edit")

    matches = matchings(request.user)

    return render(request, "pages/myroom.html", {"matches": matches})


def user_logout(request):
    """Log out and redirect to Home Page"""
    logout(request)
    messages.error(request, "Logged out successfully!")
    return redirect("home")
