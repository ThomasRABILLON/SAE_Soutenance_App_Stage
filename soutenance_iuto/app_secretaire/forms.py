from django import forms

from common.models.Soutenance import Soutenance

class SoutenanceForm(forms.ModelForm):
    class Meta:
        model = Soutenance
        fields = ['stg_alt', 'horaire', 'salle', 'prof_candide']
        labels = {
            'stg_alt': 'Stage alternance',
            'horaire': 'Date et horaire',
            'salle': 'Salle',
            'prof_candide': 'Professeur candidat'
        }
        widgets = {
            'stg_alt': forms.Select(attrs={'class': 'form-control'}),
            'horaire': forms.Select(attrs={'class': 'form-control'}),
            'salle': forms.Select(attrs={'class': 'form-control'}),
            'prof_candide': forms.Select(attrs={'class': 'form-control'})
        }