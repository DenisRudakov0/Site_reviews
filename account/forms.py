from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': "form-control"}))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class': "form-control"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs = {'class': "form-control"}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': TextInput(attrs = {'class': "form-control"}),
            'first_name': TextInput(attrs = {'class': "form-control"}),
            'email': TextInput(attrs = {'class': "form-control"}),
        }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Пользователь с таким email уже зарегестрирован')
        return email