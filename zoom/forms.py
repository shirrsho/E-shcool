from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    # def save(li,self, commit=True):
    #     obj = super(MeetingForm, self).save(commit=False)
    #     obj.infos = li
    #     if commit:
    #         obj.save()
    #     return obj
    class Meta:
        model = Meeting
        fields = ('title','dates','times')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'dates': forms.TextInput(attrs={'class': 'form-control'}),
            'times': forms.TextInput(attrs={'class': 'form-control'})
        }

