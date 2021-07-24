from hoodalert.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from hoodalert.forms import LoginForm, RegisterUserForm, UserProfileForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

#register User
def register_user(request):
  title = 'create account'
  form = RegisterUserForm
  if request.method == 'POST':
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      form.save()

      return redirect('login_user')
      
  context = {
    'form':form,
    'title':title
  }
  return render(request, 'django_registration/registration_form.html', context)

#login user
def login_user(request):
  title = 'Login to Your Account'
  form = LoginForm
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    newlogin =  authenticate(request, username = username, password = password)

    if newlogin is not None:
      login(request, newlogin)

      return redirect('/')
    else:
      messages.warning(request, 'Incorrect Username or Password')
  
  context = {
    'title':title,
    'form':form,
  }
  return render(request, 'registration/login.html', context)

#logout view function
def logout_user(request):
  '''
  logout a logged in user
  '''
  logout(request)

  return redirect('login_user')
#view function to user profile
def add_user_profile(request):
  '''
  form to update user profile
  '''
  title = f'{request.user.username}\'s Profile - Hood alert'
  form = UserProfileForm
  try:
    profile = UserProfile.objects.filter(user = request.user).last()
  except UserProfile.DoesNotExist:
    profile = None
  if request.method == 'POST':
    form = UserProfileForm(request.POST, request.FILES)
    if form.is_valid():
      new_profile = form.save(commit = False)
      new_profile.user = request.user
      new_profile.save()

      context = {
        'title':title,
        'form':form,
        'profile':profile,
      }
      return render(request, 'all_templates/profile.html', context)
  else:
    context = {
      'title':title,
      'form':form,
      'profile':profile,
      }
    return render(request, 'all_templates/profile.html', context)

#view function to homepage
def index(request):
  title = 'Home - Neighbourhood Alert'

  context = {
    'title':title,
  }

  return render(request, 'all_templates/index.html', context)
