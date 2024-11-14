from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Регистрация модели CustomUser в админке
admin.site.register(CustomUser, UserAdmin)
