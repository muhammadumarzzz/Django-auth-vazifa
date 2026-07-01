from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

# ─────────────────────────────────────────────────────────────
# MASALA 2: LoginView va LogoutView ni URL ga ulash
# ─────────────────────────────────────────────────────────────
# LoginView:
#   - GET:  login.html shablonini ko'rsatadi
#   - POST: username/parolni tekshiradi, login qiladi
#
# LogoutView:
#   - POST: sessionni o'chiradi, logout qiladi
#   - LOGOUT_REDIRECT_URL ga yo'naltiradi
#
urlpatterns = [
    # Bosh sahifa
    path('', views.home, name='home'),

    # Login / Logout
    path('accounts/login/',  LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # Ro'yxatdan o'tish
    path('register/', views.register, name='register'),

    # Himoyalangan sahifalar
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/',   views.profile,   name='profile'),
    path('settings/',  views.SettingsView.as_view(), name='settings'),
]
