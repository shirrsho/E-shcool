from django import forms
from .models import Assignment, Solution


class DateInput(forms.DateInput):
    input_type = 'date'



class AssignmentForm(forms.ModelForm):
    title = forms.CharField(
        label='Name',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Enter Assignment Name',
            'class':'form-control'
            }))

    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '6',
            'placeholder': 'Say Something...',
            'class':'form-control'
            }))


    class Meta:
        model = Assignment
        fields = ('title', 'body', 'question', 'due')
        widgets = {
            'due': DateInput(),
        }



class SolutionForm(forms.ModelForm):
    answer = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Write your Answer here...',
                   'class':'form-control'
                   }
        ))

    class Meta:
        model = Solution
        fields = ['answer']
