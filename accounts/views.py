"""
accounts/views.py
─────────────────
Bu faylda quyidagi view lar bor:

  home()        → Masala 11: Bosh sahifa (hammaga ochiq)
  register()    → Masala 5, 6, 7: Ro'yxatdan o'tish
  dashboard()   → Masala 8: @login_required bilan himoyalangan
  profile()     → Masala 9: Foydalanuvchi ma'lumotlari
  SettingsView  → Masala 10: CBV + LoginRequiredMixin
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import login

from .forms import CustomRegisterForm


# ─────────────────────────────────────────────────────────────────────────────
# MASALA 11: Bosh sahifa
# ─────────────────────────────────────────────────────────────────────────────
def home(request):
    """
    Bosh sahifa — hammaga ochiq.

    Template (home.html) da login holatiga qarab tarkib ko'rsating:
      - Login bo'lgan: 'Salom, {{ user.username }}!' + Chiqish
      - Login bo'lmagan: Kirish + Ro'yxatdan o'tish havolalari

    Ko'rsatma: {% if user.is_authenticated %} ... {% else %} ... {% endif %}
    """
    return render(request, 'home.html')


# ─────────────────────────────────────────────────────────────────────────────
# MASALA 5, 6, 7: Ro'yxatdan o'tish
# ─────────────────────────────────────────────────────────────────────────────
def register(request):
    """
    Ro'yxatdan o'tish view.

    Masala 5: Oddiy ro'yxatdan o'tish
    Masala 6: Email maydonli forma (CustomRegisterForm)
    Masala 7: Ro'yxatdan o'tgandan so'ng avtomatik login

    TODO (bosqichma-bosqich):
    1. POST so'rovda CustomRegisterForm(request.POST) bilan forma yarating
    2. form.is_valid() tekshirib ko'ring
    3. user = form.save() — foydalanuvchini saqlang
    4. (Masala 7) login(request, user) — avtomatik login
    5. return redirect('dashboard') — yo'naltiring
    """
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            # TODO: Masala 5 — foydalanuvchini saqlang
            # user = form.save()

            # TODO: Masala 7 — Avtomatik login
            # login(request, user)

            # TODO: Masala 5/7 — Yo'naltiring
            # return redirect('dashboard')

            # Shu qatorni olib tashlang, TODO larni bajaring

            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = CustomRegisterForm()

    return render(request, 'registration/register.html', {'form': form})


# ─────────────────────────────────────────────────────────────────────────────
# MASALA 8: Dashboard — @login_required
# ─────────────────────────────────────────────────────────────────────────────
# TODO: @login_required decoratorini bu yerga qo'shing!
# Decorator:  @login_required
def dashboard(request):
    """
    Dashboard sahifasi.

    @login_required: Foydalanuvchi login bo'lmagan bo'lsa,
    avtomatik ravishda LOGIN_URL ga yo'naltiriladi.

    Test qiling:
    1. Login holida: /dashboard/ → ko'rinishi kerak
    2. Logout holida: /dashboard/ → /accounts/login/ ga yo'naltirilishi kerak

    TODO: @login_required decoratorini qo'shing (yuqoridagi izoh).
    """
    return render(request, 'dashboard.html', {'user': request.user})


# ─────────────────────────────────────────────────────────────────────────────
# MASALA 9: Profil sahifasi
# ─────────────────────────────────────────────────────────────────────────────
@login_required
def profile(request):
    """
    Profil sahifasi.

    Template da quyidagi ma'lumotlarni ko'rsating:
      - {{ user.username }}
      - {{ user.email }}
      - {{ user.date_joined }}      ← Ro'yxatdan o'tgan sana
      - {{ user.last_login }}       ← Oxirgi kirish sanasi
      - {{ user.is_superuser }}     ← Superuser yoki yo'q

    TODO: profile.html templateni to'ldiring.
    """
    return render(request, 'profile.html', {'user': request.user})


# ─────────────────────────────────────────────────────────────────────────────
# MASALA 10: Class-based view — LoginRequiredMixin
# ─────────────────────────────────────────────────────────────────────────────
class SettingsView(LoginRequiredMixin, TemplateView):
    """
    Sozlamalar sahifasi — Class-based view.

    LoginRequiredMixin — bu @login_required ning class-based view versiyasi.
    Ishlash tartibi bir xil:
      - Login bo'lmagan foydalanuvchi login_url ga yo'naltiriladi.

    TODO: settings.html templateni to'ldiring.
    """
    template_name = 'settings.html'
    login_url = '/accounts/login/'
