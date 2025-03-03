# polls/forms.py
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)  # Створюємо користувача, але ще не зберігаємо
        user.set_password(self.cleaned_data['password'])  # Використовуємо set_password для шифрування пароля
        if commit:
            user.save()  # Тепер зберігаємо користувача з зашифрованим паролем
        return user


