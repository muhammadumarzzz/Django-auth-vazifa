from django.contrib import admin
from django.contrib.auth.models import User

# Django standart User modeli admin ga avtomatik ro'yxatdan o'tgan.
# Qo'shimcha sozlash uchun:
#
# from django.contrib.auth.admin import UserAdmin
# admin.site.unregister(User)
#
# @admin.register(User)
# class MyUserAdmin(UserAdmin):
#     list_display = ['username', 'email', 'is_staff', 'date_joined']
