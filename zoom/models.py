from django.db import models

# Create your models here.

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    dates = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    infos = models.CharField(max_length=500, default="null")

    def __str__(self):
        return self.title
