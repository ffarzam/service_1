from django.contrib import admin

# Register your models here.
from .models import Site, City, Province

admin.site.register(Site)
admin.site.register(City)
admin.site.register(Province)