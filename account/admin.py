from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User,Profile
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','full_name','email','is_staff','is_superuser','is_active']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','user','image']