"""
auth_project sozlamalari
Django 4.2+
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ─────────────────────────────────────────────────────────────
# DIQQAT: Haqiqiy loyihada bu kalitni yashiring! (.env fayl)
SECRET_KEY = 'django-insecure-change-this-in-production-keep-secret'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ─────────────────────────────────────────────────────────────
# O'RNATILGAN ILOVALAR
# ─────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',           # Admin panel
    'django.contrib.auth',            # Autentifikatsiya tizimi ← ASOSIY
    'django.contrib.contenttypes',    # Content types (permissions uchun kerak)
    'django.contrib.sessions',        # Session boshqaruvi
    'django.contrib.messages',        # Xabar tizimi
    'django.contrib.staticfiles',     # Statik fayllar

    # Bizning ilovalarimiz:
    'accounts',   # 2-5 qismlar: Login, Register, Dashboard
    'blog',       # 5-qism: Post, Guruhlar, Permissions
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',   # ← Request ga user qo'shadi
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'auth_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # ← Umumiy templates papkasi
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',    # ← {{ user }} ni beради
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'auth_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─────────────────────────────────────────────────────────────
# MASALA 3: Authentication URL sozlamalari
# ─────────────────────────────────────────────────────────────
#
#   LOGIN_URL:
#   Foydalanuvchi himoyalangan sahifaga kirishga urinsa,
#   Django uni shu URL ga yo'naltiradi.
#   (@login_required decorator ishlatadi)
#
LOGIN_URL = '/accounts/login/'

#   LOGIN_REDIRECT_URL:
#   Login muvaffaqiyatli bo'lgandan keyin
#   foydalanuvchi shu URL ga yo'naltiriladi.
#
LOGIN_REDIRECT_URL = '/dashboard/'

#   LOGOUT_REDIRECT_URL:
#   Logout qilgandan keyin shu URL ga yo'naltiriladi.
#
LOGOUT_REDIRECT_URL = '/'
