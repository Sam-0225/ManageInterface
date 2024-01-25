from django.db import models

class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=255, default='My Campsite')
    welcome_message = models.TextField(null=True, blank=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.site_name