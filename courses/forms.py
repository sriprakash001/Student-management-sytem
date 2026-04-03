from django import forms
from .models import Course

class course_forms(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
           "name":forms.TextInput(attrs={'class':'form-control'}),
           "code":forms.TextInput(attrs={'class':'form-control'}),
           "description":forms.Textarea(attrs={'class':'form-control'})
        }