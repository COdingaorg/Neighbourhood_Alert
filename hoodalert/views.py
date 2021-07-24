from django.shortcuts import render

# Create your views here.
def index(request):
  title = 'Home - Neighbourhood Alert'

  context = {
    'title':title,
  }

  return render(request, 'all_templates/index.html', context)
