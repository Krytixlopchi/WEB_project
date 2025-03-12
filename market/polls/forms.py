from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Image

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'enter your password'}),
        help_text="",
        label="Password"
    )
    
    # Додаємо поле для підтвердження пароля
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'confirm your password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'enter your username',
                'autofocus': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'enter your email',
                'required': True
            }),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
        }

    # Валідація пароля
    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password, self.instance)
        except ValidationError as e:
            raise forms.ValidationError(list(e.messages))
        
        return password

    # Валідація підтвердження пароля
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user