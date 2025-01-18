from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    # Add fields to the admin interface
    # so that we can see the email and username in /admin route
    model = UserProfile
    list_display = ['email', 'username']