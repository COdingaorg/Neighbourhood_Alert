from hoodalert.models import Business, HealthDep, Neighbourhood, PoliceDep, Posts, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from hoodalert.forms import AddBusiness, AddPost, LoginForm, RegisterUserForm, UserProfileForm
from django.shortcuts import redirect, render
from django.contrib import messages
import datetime as dt

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
      new_profile.save_profile()

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

def index(request):
  '''
  renders user profile
  renders businesses that exist in the users hood
  renders posts, all posts created
  renders add post form
  renders neighbourhood details
  renders police_stns
  renders hospitals
  renders neighbourhood members
  renders add business form
  '''
  form = AddPost
  #---------------------------------------------
  #render Form add post
  if request.method == 'POST':
    form = AddPost(request.POST, request.FILES)
    try:
      user_profile = UserProfile.get_user_profile(request.user)
    except UserProfile.DoesNotExist:
      user_profile = None
   
    if user_profile is not None:
      if form.is_valid():
        new_post = form.save(commit=False)
        
        new_post.poster = user_profile
        new_post.date_created = dt.datetime.utcnow()
        new_post.save()

        context = {
          'form':form,
          }
        messages.success(request, 'Post Created Successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      else:
        messages.warning(request, 'Invalid Data')
    else:
      messages.warning(request, 'You need a User Profile to Add Post')
      return redirect('add_profile')
  #-------------------------------------------------------
  #-------------------------------------------------------
  #start of add business form
  form_buss = AddBusiness
  if request.method == 'POST':
    form_buss = AddBusiness(request.POST)
    try:
      user_profile = UserProfile.get_user_profile(request.user)
    except UserProfile.DoesNotExist:
      user_profile = None

    if user_profile is not None:
      if form_buss.is_valid():
        new_business = form_buss.save(commit=False)
        new_business.owner_user_prof = user_profile
        new_business.neighborhood = user_profile.hood
        new_business.save()

        messages.success(request, 'Business Added Successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      
      else:
        messages.warning(request, 'Invalid Form')
    else:
      messages.warning(request, 'You need a profile to create a business')
      return redirect('user_profile')

    #-------------------------------------------------------------------------------------
  else:

    title = 'Home - Neighbourhood Alert'
    try:
      user_profile = UserProfile.get_user_profile(request.user)
    except UserProfile.DoesNotExist:
      user_profile = None
    
    try:
      businesses = Business.objects.filter(neighborhood = user_profile.hood)
    except Business.DoesNotExist:
      businesses = None

    try:
      posts = Posts.objects.all()
    except Posts.DoesNotExist:
      posts = None

    try:
      neighborhood = Neighbourhood.objects.get(name = user_profile.hood.name)
    except Posts.DoesNotExist:
      neighborhood = None

    try:
      members = UserProfile.objects.filter(hood = user_profile.hood)
    except UserProfile.DoesNotExist:
      members = None

    date_today = dt.date.today()
      
    context = {
      'form_buss':form_buss,
      'date_today':date_today,
      'members':members,
      'neighborhood':neighborhood,
      'form':form,
      'posts':posts,
      'businesses':businesses,
      'user_profile':user_profile,  
      'title':title,
    }

    return render(request, 'all_templates/index.html', context)
