from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    """
    MASALA 6: Email maydoni qo'shilgan ro'yxatdan o'tish formasi.

    UserCreationForm standart holda faqat username, password1, password2 beradi.
    Biz unga email maydonini qo'shamiz.

    TODO:
    1. email maydonini qo'shing (required=True)
    2. Meta class da fields ni to'g'rilang
    """

    # TODO: email maydonini bu yerga qo'shing
    # email = forms.EmailField(...)

    class Meta:
        model = User
        # TODO: fields ga 'email' ni qo'shing
        fields = ['username', 'email', 'password1', 'password2']
        # KERAK: fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Formani o'zbekchalashtirish (ixtiyoriy)
        self.fields['username'].help_text = 'Faqat harf, raqam va @ . + - _ belgilari.'
        self.fields['email'].help_text = "Email kiriting va @ . belgilari bo'lishi shart."
        self.fields['password1'].help_text = 'Kamida 8 ta belgi. Oddiy paroldan foydalanmang.'
        self.fields['password2'].help_text = 'Tasdiqlash uchun xuddi yuqoridagi parolni kiriting.'
