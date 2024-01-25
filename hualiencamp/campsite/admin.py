from django.contrib import admin

from .models import Campsite

class CampsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'map_image')

admin.site.register(Campsite, CampsiteAdmin)