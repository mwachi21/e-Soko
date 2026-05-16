from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileUpdateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("profile")
    template_name = "registration/profile_update.html"

@login_required
def profile(request):
    return render(request, "registration/users_hub/profile.html")
