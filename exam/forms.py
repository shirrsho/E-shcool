from django import forms
from .models import Exam, ExamSolution


class DateInput(forms.DateInput):
    input_type = 'date'



class ExamForm(forms.ModelForm):
    title = forms.CharField(
        label='Name',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Enter Exam Name',
            'class':'form-control'
            }))

    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...',
            'class':'form-control'
            }))

    sampleSol = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '5',
            'placeholder': 'Enter Sample Solution here...',
            'class':'form-control'
            }))


    class Meta:
        model = Exam
        fields = ('title', 'body', 'question','sampleSol', 'due')
        widgets = {
            'due': DateInput(),
        }



class ExamSolutionForm(forms.ModelForm):
    answer = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '5',
                   'placeholder': 'Write your Answer here...',
                   'class':'form-control'}
        ))

    class Meta:
        model = ExamSolution
        fields = ['answer']
