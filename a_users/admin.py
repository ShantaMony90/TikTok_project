from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  fieldsets = (
    (None, {'fields': ('name', 'image', 'bio', 'birthday')}),
    ) + UserAdmin.fieldsets
  list_display = ('username', 'name', 'email', 'is_staff')
