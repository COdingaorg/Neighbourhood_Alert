from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import fields
from .models import Business, Posts, User, UserProfile
from hoodalert import models

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
    fields = ('photo_path', 'about', 'hood', 'location_description')

class AddBusiness(forms.ModelForm):
  class Meta:
    model = Business
    fields = ('name', 'email', 'location_or_Description')

class AddPost(forms.ModelForm):
  class Meta:
    model = Posts
    widgets = {
      'title':forms.TextInput(attrs={
        'placeholder':'What is your Post about...',
        'class':'title_input'}),
      'description':forms.Textarea(attrs={
        'placeholder':'Tell us ...',
        'class':'desc_input',
        }),
    }
    fields = ['title', 'description', 'post_image']

class ChangeHood(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ['hood']