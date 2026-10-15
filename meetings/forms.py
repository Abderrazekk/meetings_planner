from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Affiche un sélecteur de date HTML5
        }