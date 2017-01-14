from django import forms
from lab_7.models import *
from django.contrib.auth.hashers import make_password


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}), \
                               min_length=5, label='Логин:')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}), \
                           max_length=30, label='Имя:')
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'surname'}), \
                              max_length=30, label='Фамилия:')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}), label='Email')
    password = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),\
                                min_length=8, label='Пароль:')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2'}),\
                                min_length=8, label='Повторите пароль:')

    def clean_password2(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError ('Passwords does not match')

    def save(self):
        u = User()
        u.username = self.cleaned_data.get('username')
        u.password = make_password(self.cleaned_data.get('password'))
        u.first_name = self.cleaned_data.get('name')
        u.last_name = self.cleaned_data.get('surname')
        u.email = self.cleaned_data.get('email')
        u.is_staff = False
        u.is_active = True
        u.is_superuser = False
        u.save()

    def clean_username(self):
        username=self.cleaned_data.get('username')
        try:
            u=User.objects.get(username=username)
            raise forms.ValidationError('This login already uses')
        except User.DoesNotExist:
            return username



