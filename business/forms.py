from django import forms
from .models import StaffAvailability

class AvailabilityForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': '{% now "Y-m-d" %}'
        }),
        label='Tarih'
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control'
        }),
        label='Başlangıç Saati'
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control'
        }),
        label='Bitiş Saati'
    )
    
    class Meta:
        model = StaffAvailability
        fields = ['date', 'start_time', 'end_time', 'is_available']
        widgets = {
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'is_available': 'Müsait'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError('Bitiş saati başlangıç saatinden sonra olmalıdır.')
        
        return cleaned_data
