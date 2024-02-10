from django.contrib import admin

from .models import SiteConfiguration

class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'welcome_message', 'contact_email')

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)