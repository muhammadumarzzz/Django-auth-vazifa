"""
MASALA 12: Post modeli

5-qismda kerak: Blog post va Permissions tizimi.
"""
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Matn')

    # settings.AUTH_USER_MODEL — Custom User bilan ishlashga imkon beradi
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Muallif'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'

    def __str__(self):
        return self.title
