from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registrieren des CustomUser-Modells im Admin
admin.site.register(CustomUser, UserAdmin)
