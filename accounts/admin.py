from multiprocessing.util import info

from django.contrib import admin
from accounts.models import Profile
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Profile)
admin.site.unregister(Group)

# Mix Profile info into user info
class ProfileInline(admin.StackedInline):
   model = Profile

# Extend user Model
