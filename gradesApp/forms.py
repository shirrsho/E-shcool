from django import forms
from django.contrib.auth.models import User
from gradesApp.models import Student,Teacher, UserProfile

class studentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }

BRANCH_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),

)
class studentAddForm(forms.ModelForm):
    semester=forms.CharField(widget=forms.Select(choices=BRANCH_CHOICES))
    class Meta():
        model=Student
        fields=['idno','semester']
        widgets = {
            'idno': forms.NumberInput(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'})
        }

class teacherForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }

class teacherAddForm(forms.ModelForm):
    class Meta():
        model=Teacher
        fields=['phone']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'})
        }


class EditProfile(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields = "__all__"
        exclude = ('user',)
