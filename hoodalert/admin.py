from django.contrib import admin
from django.http.response import HttpResponseRedirect
from hoodalert.models import HealthDep, Neighbourhood, PoliceDep

# Register your models here.
admin.site.register(HealthDep)
admin.site.register(PoliceDep)
admin.site.register(Neighbourhood)
