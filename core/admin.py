from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Todo

@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    # Add fields to the admin interface
    # so that we can see the email and username in /admin route
    model = UserProfile
    list_display = ['email', 'username']

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'user']
    list_filter = ['is_completed']
    search_fields = ['title']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 10
