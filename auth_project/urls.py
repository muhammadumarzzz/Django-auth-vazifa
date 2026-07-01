"""
auth_project URL Configuration

URL lashtirishni accounts va blog ilovalariga topshiramiz.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Accounts (login, logout, register, dashboard, profile)
    path('', include('accounts.urls')),

    # Blog (post list, detail, add, edit, delete)
    path('blog/', include('blog.urls')),
]
