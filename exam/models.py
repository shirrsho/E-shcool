from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Exam(models.Model):
    title = models.TextField()
    body = models.TextField()
    sampleSolution = models.TextField()
    due = models.DateField()
    question = models.FileField(upload_to='exams/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ExamSolution(models.Model):
    answer = models.TextField()
    submission_time = models.DateTimeField(default=timezone.now)
    problem = models.ForeignKey('Exam', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
