from django.contrib import admin
from .models import CariclumVitae

# Register your models here.

class CariclumVitaeAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(CariclumVitae)