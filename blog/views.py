"""
MASALA 14: @permission_required bilan himoyalangan view lar

Shell buyruqlari (Masala 13):
─────────────────────────────
python manage.py shell

>>> from django.contrib.auth.models import Group, Permission, User
>>> from django.contrib.contenttypes.models import ContentType
>>> from blog.models import Post
>>>
>>> # 1. Editors guruhini yarating
>>> editors = Group.objects.create(name='Editors')
>>>
>>> # 2. Post modelining barcha ruxsatlarini bering
>>> ct = ContentType.objects.get_for_model(Post)
>>> perms = Permission.objects.filter(content_type=ct)
>>> editors.permissions.set(perms)
>>> print('Ruxsatlar:', list(perms.values_list('codename', flat=True)))
>>>
>>> # 3. Ali ni Editors guruhiga qo'shing
>>> ali = User.objects.get(username='ali')
>>> ali.groups.add(editors)
>>> print('Ali guruhlari:', ali.groups.all())
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Post


def post_list(request):
    """Barcha postlar — hamma ko'ra oladi."""
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Post detali — hamma ko'ra oladi."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# ─────────────────────────────────────────────────────────────────────────────
# MASALA 14: Permission bilan himoyalangan view lar
# ─────────────────────────────────────────────────────────────────────────────

@permission_required('blog.add_post', raise_exception=True)
def add_post(request):
    """
    Post qo'shish — faqat blog.add_post ruxsati bo'lgan foydalanuvchilar.

    raise_exception=True:
      - Ruxsat bo'lmasa → 403 Forbidden qaytaradi
      - False bo'lsa → login sahifasiga yo'naltiradi

    Test:
      - Ali (Editors): post qo'sha oladi ✓
      - Hasan (guruhi yo'q): 403 xato ✓

    TODO: Bu view ga forma qo'shing (PostForm).
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, content=content, author=request.user)
            messages.success(request, 'Post muvaffaqiyatli qo\'shildi!')
            return redirect('post_list')

    return render(request, 'blog/post_form.html', {'action': 'Qo\'shish'})


@permission_required('blog.change_post', raise_exception=True)
def edit_post(request, pk):
    """
    Post tahrirlash — faqat blog.change_post ruxsati bo'lgan foydalanuvchilar.

    TODO: Mavjud post ma'lumotlarini forma bilan to'ldiring.
    """
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title', post.title)
        post.content = request.POST.get('content', post.content)
        post.save()
        messages.success(request, 'Post yangilandi!')
        return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_form.html', {'post': post, 'action': 'Tahrirlash'})


@permission_required('blog.delete_post', raise_exception=True)
def delete_post(request, pk):
    """
    Post o'chirish — faqat blog.delete_post ruxsati bo'lgan foydalanuvchilar.

    Test qiling va screenshot oling:
      - Ali (Editors): o'chira oladi ✓
      - Hasan (ruxsat yo'q): 403 xato chiqadi ✓
    """
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post o\'chirildi!')
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})
