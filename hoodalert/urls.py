from django.conf.urls import url
from hoodalert import views

urlpatterns = [
  url('', views.index, name= 'home'),
]