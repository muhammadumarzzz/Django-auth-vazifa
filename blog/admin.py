from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'created_at']
    search_fields = ['title', 'content']

    # Admin panelda post yaratishda muallif avtomatik aniqlansin
    def save_model(self, request, obj, form, change):
        if not obj.pk:          # yangi post bo'lsa
            obj.author = request.user
        super().save_model(request, obj, form, change)
