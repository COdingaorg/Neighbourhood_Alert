from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, UserProfile

class RegisterUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ['__all__']

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('photo_path', 'bio')
