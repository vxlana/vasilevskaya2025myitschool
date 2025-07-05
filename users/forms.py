from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1 and len(password1) < 8:
            self.add_error('password1', 'Минимум 8 символов.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        return password2

class UserLoginForm(AuthenticationForm):
    pass

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'middle_name',
            'city', 'street', 'house_number',
            'apartment_number', 'postal_code',
        ]
