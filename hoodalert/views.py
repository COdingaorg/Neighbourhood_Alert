from hoodalert.forms import RegisterUserForm
from django.shortcuts import render

# Create your views here.

#register User
def register_user(request):
  title = 'create account'
  form = RegisterUserForm
  if request.method == 'POST':
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      form.save()
      
  context = {
    'form':form,
    'title':title
  }
  return render(request, 'django_registration/registration_form.html', context)
def index(request):
  title = 'Home - Neighbourhood Alert'

  context = {
    'title':title,
  }

  return render(request, 'all_templates/index.html', context)
