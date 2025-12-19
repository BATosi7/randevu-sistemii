from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment, Rating

class AppointmentForm(forms.ModelForm):
    TIME_CHOICES = [
        ('09:00', '09:00'), ('09:30', '09:30'),
        ('10:00', '10:00'), ('10:30', '10:30'),
        ('11:00', '11:00'), ('11:30', '11:30'),
        ('12:00', '12:00'), ('12:30', '12:30'),
        ('13:00', '13:00'), ('13:30', '13:30'),
        ('14:00', '14:00'), ('14:30', '14:30'),
        ('15:00', '15:00'), ('15:30', '15:30'),
        ('16:00', '16:00'), ('16:30', '16:30'),
        ('17:00', '17:00'), ('17:30', '17:30'),
        ('18:00', '18:00'),
    ]
    time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'min': '{% now "Y-m-d" %}'  # This will be rendered in template
            }),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        # Set min date dynamically
        from datetime import date
        self.fields['date'].widget.attrs['min'] = date.today().strftime('%Y-%m-%d')

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # Check if date is in the past
        if date:
            from datetime import date as dt_date
            if date < dt_date.today():
                raise ValidationError("Geçmiş bir tarihe randevu alamazsınız. Lütfen bugün veya gelecek bir tarih seçin.")

        if date and time and self.company:
            # Check for conflicting appointments
            # We exclude cancelled, no_show, and maybe rejected? Let's say cancelled and no_show are definitely free.
            # Assuming 'pending' and 'confirmed' block the slot.
            conflicts = Appointment.objects.filter(
                company=self.company,
                date=date,
                time=time,
                status__in=['pending', 'confirmed', 'completed']
            )

            if conflicts.exists():
                raise ValidationError("Bu tarih ve saatte başka bir randevu mevcuttur. Lütfen başka bir saat seçiniz.")
        
        return cleaned_data

class RatingForm(forms.ModelForm):
    SCORE_CHOICES = [
        (5, '⭐⭐⭐⭐⭐ Mükemmel'),
        (4, '⭐⭐⭐⭐ Çok İyi'),
        (3, '⭐⭐⭐ İyi'),
        (2, '⭐⭐ Orta'),
        (1, '⭐ Kötü'),
    ]
    
    score = forms.ChoiceField(
        choices=SCORE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Puanınız'
    )
    
    class Meta:
        model = Rating
        fields = ['score', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Deneyiminizi bizimle paylaşın... (Opsiyonel)'
            })
        }
        labels = {
            'comment': 'Yorumunuz'
        }
