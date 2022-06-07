from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    semester=models.CharField(max_length=256,blank=False)
    is_student=models.BooleanField(default=True)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    is_student=models.BooleanField(default=False)

    def __str__(self):
        return self.teacher.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    attendance = models.IntegerField()
