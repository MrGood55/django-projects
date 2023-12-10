# В файле forms.py вашего приложения
from django import forms
from .models import Product
from app.models import Product, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Klient,User,Manager




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Категория'

    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Категория'
        }




class KlientRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = Klient
        fields = ('username', 'email', 'password1', 'password2')  # Add other fields if needed

    def save(self, commit=True):
        user = super().save(commit=False)
        user.base_role = User.Role.KLIENT  # Set the role to KLIENT
        if commit:
            user.save()
        return user

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))






class AdminRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = Klient
        fields = ('username', 'email', 'password1', 'password2')  # Add other fields if needed

    def save(self, commit=True):
        user = super().save(commit=False)
        user.base_role = User.Role.MANAGER  # Set the role to KLIENT
        if commit:
            user.save()
        return user