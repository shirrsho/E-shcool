from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=100)
    noticeDate = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.title
