from django.db import models

class Campsite(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    map_image = models.ImageField(upload_to='campsite/maps/')
    # 其他字段根據需求添加

    def __str__(self):
        return self.name