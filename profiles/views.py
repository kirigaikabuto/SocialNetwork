from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm


def register_page(request):
    user_form = None
    profile_form = None
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            my_user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = my_user
            profile.save()
            return HttpResponse("ok")

    user_form = UserCreationForm()
    profile_form = ProfileCreationForm()
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "profiles/register.html", context=context)
