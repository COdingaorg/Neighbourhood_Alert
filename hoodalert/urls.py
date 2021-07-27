from django.conf.urls import url
from hoodalert import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.index, name= 'home'),
  url(r'^register_user/$', views.register_user, name = 'register_user'),
  url(r'^login_user/$', views.login_user, name = 'login_user'),
  url(r'^logout_user/$', views.logout_user, name = 'logout_user'),
  url(r'^profile/$', views.add_user_profile, name = 'user_profile'),
  url(r'^search_business/$', views.search_business, name = 'search_business'),
  url(r'^change_hood/$', views.change_hood, name = 'change_hood'),
]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)