from django.contrib import admin

# Register your models here.

from .models import Company, Location, Language, Programmer

admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Language)
admin.site.register(Programmer)