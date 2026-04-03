from django import forms
from .models import Student,Enrollment,Attendence
from  django.forms import modelformset_factory

class student_forms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','phone','date_of_birth']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'data_of_birth':forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

class Enrollment_forms(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student','course']
        
        widgets = {
            'student':forms.Select(attrs={'class':'form-control'}),
            'course':forms.Select(attrs={'class':'form-control'}),
        }

# Attendence form 
class Attendence_forms(forms.ModelForm):
    class Meta:
        model = Attendence
        fields = ['student','status']

        widgets = {
            'student':forms.HiddenInput(),
            'status':forms.Select(attrs={'class':'form-select'}),
        }

AttendenceFormSet = modelformset_factory(
    Attendence,
    form=Attendence_forms,
    extra=0
)