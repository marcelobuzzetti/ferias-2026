from django import forms
from .models import Ferias

class FeriasForm(forms.ModelForm):
    class Meta:
        model = Ferias
        fields = [
            'promo_nr', 'posto_graduacao', 'nome_guerra', 'tipo_carreira',
            'secao', 'substituto', 'habilitacao', 'periodo_aquisitivo',
            'data_inicio', 'data_termino', 'data_apresentacao'
        ]
        widgets = {
            'promo_nr': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2, 13...'}),
            'posto_graduacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: CAP, SGT...'}),
            'nome_guerra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de guerra'}),
            'tipo_carreira': forms.Select(attrs={'class': 'form-control'}),
            'secao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: GARAGEM, PEL COM...'}),
            'substituto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Substituto'}),
            'habilitacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: B, D...'}),
            'periodo_aquisitivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2024, 2025...'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_apresentacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
