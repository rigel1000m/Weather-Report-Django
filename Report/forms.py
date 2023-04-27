from .models import LastReport
from django.forms import ModelForm, TextInput


class LastReportForms(ModelForm):
    class Meta:
        model = LastReport
        fields = ['city']
        widgets = {
            'city': TextInput(attrs={
                'class': 'form-control',
                'id': 'city',
                'name': 'city',
                'placeholder': 'Введите город'
            })
        }
