# Django Authentication — Uyga Vazifa Starter Kit

> **IT Shaharcha** | Amaliy topshiriq uchun tayyor shablon

---

## 📁 Loyiha tuzilishi

```
django-auth-vazifa/
│
├── 1-qism-javoblar/          ← 1-Qism: Nazariy savollar
│   └── javoblar.md           ← Bu faylni to'ldiring!
│
├── auth_project/             ← 2-5 Qismlar
│   ├── accounts/             ← Login, Register, Dashboard
│   ├── blog/                 ← Post, Guruhlar, Permissions
│   └── templates/            ← HTML fayllar
│
├── auth_project_v2/          ← 6-7 Qismlar
│   ├── accounts/             ← Custom User (AbstractUser)
│   ├── profiles/             ← Profile + Signal
│   └── templates/
│
├── blog_platform/            ← 8-Qism (Yakuniy loyiha)
│   ├── accounts/             ← Email login
│   ├── profiles/             ← Profile
│   ├── blog/                 ← Post, Comment
│   └── templates/
│
├── screenshots/              ← Test screenshotlari
├── BOSHLASH.md               ← Tezkor boshlash ko'rsatmasi
├── .gitignore
└── README.md                 ← Bu fayl
```

---

## 🛠️ O'rnatish (bir marta)

```bash
# 1. Virtual muhit
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac / Linux:
source venv/bin/activate

# 2. Kutubxonalar
pip install django pillow
```

---

## 🚀 Har bir loyihani ishga tushirish

### auth_project (2-5 Qismlar)
```bash
cd auth_project
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
→ http://127.0.0.1:8000/

### auth_project_v2 (6-7 Qismlar)
```bash
cd auth_project_v2
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # email kiritish kerak bo'ladi
python manage.py runserver
```

### blog_platform (8-Qism)
```bash
cd blog_platform
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## ✏️ Nima qilish kerak?

Fayllar ichida barcha `# TODO:` va `TODO:` belgilarini toping va to'ldiring.

### 1-Qism: Nazariy savollar
- `1-qism-javoblar/javoblar.md` faylini oching
- 8 ta savolga **o'z so'zlaringiz bilan** javob yozing

### 2-Qism: Authentication
- `auth_project/accounts/views.py` → `register()` view ni to'ldiring
- `auth_project/accounts/forms.py` → email maydonini qo'shing
- Admin da Ali, Hasan, Lola yarating

### 3-Qism: Registration
- `register()` view da `form.save()` va `login()` qo'shing

### 4-Qism: @login_required
- `dashboard` view ga `@login_required` qo'shing
- `profile.html` shablonni to'ldiring

### 5-Qism: Guruhlar
- Shell da "Editors" guruhini yarating
- blog/views.py ichidagi shell buyruqlarini bajaring

### 6-Qism: Custom User
- `auth_project_v2/accounts/models.py` → TODO larni bajaring
- Admin da yangi User yarating, Profile avtomatik yaratilganini tekshiring

### 7-Qism: Email login
- `blog_platform/accounts/models.py` → `USERNAME_FIELD = 'email'` qo'shing

### 8-Qism: Yakuniy loyiha
- Barcha TODO larni to'ldiring
- 3 ta guruh yarating: Readers, Authors, Moderators
- 5 ta foydalanuvchi yarating va guruhlarga qo'shing

---

## 📸 Screenshot qilish kerak

`screenshots/README.md` faylini o'qing.

---

## 📤 GitHub ga yuklash

```bash
git init
git add .
git commit -m "Django Authentication uyga vazifa"
git branch -M main
git remote add origin https://github.com/USERNAME/django-auth-vazifa.git
git push -u origin main
```

**Repository PUBLIC bo'lishi shart!**

---

## 🧪 Sinov foydalanuvchilari

| Username/Email | Parol | Guruh |
|----------------|-------|-------|
| admin | (o'zingiz o'rnating) | Superuser |
| ali | test1234 | Editors |
| hasan | test1234 | — |
| lola | test1234 | — |

---

## 🔗 Foydali havolalar

- Django hujjati: https://docs.djangoproject.com/en/stable/topics/auth/
- IT Shaharcha: https://itshaharcha.uz
"# Django-auth-vazifa" 
