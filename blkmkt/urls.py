"""
URL configuration for blkmkt project.
"""

from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # Include our accounts app URLs
    path("accounts/", include("django.contrib.auth.urls")),  # For login/logout
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
