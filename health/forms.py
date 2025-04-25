from django import forms
from .models import HealthProgram, Client

class HealthProgramForm(forms.ModelForm):
    class Meta:
        model = HealthProgram
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class EnrollClientForm(forms.ModelForm):
    enrolled_programs = forms.ModelMultipleChoiceField(
        queryset=HealthProgram.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Programs to Enroll"
    )

    class Meta:
        model = Client
        fields = ['enrolled_programs']
