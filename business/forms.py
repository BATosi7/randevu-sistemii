from django import forms
from .models import StaffAvailability, Staff
from users.models import User

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

class StaffForm(forms.ModelForm):
    # Kullanıcı bilgileri
    username = forms.CharField(
        max_length=150, 
        label='Kullanıcı Adı',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
        label='Şifre',
        required=False
    )
    first_name = forms.CharField(
        max_length=150, 
        label='Ad',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=150, 
        label='Soyad',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Staff
        fields = ['name', 'expertise']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'expertise': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Ad Soyad (Görünen)',
            'expertise': 'Uzmanlık Alanı'
        }
    
    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        
        # Eğer düzenleme modundaysa kullanıcı bilgilerini doldur
        if self.instance.pk and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['password'].help_text = 'Değiştirmek istemiyorsanız boş bırakın'
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Düzenleme modunda kendi kullanıcı adını kontrol etme
        if self.instance.pk and self.instance.user and self.instance.user.username == username:
            return username
        # Yeni kullanıcı için username kontrolü
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu kullanıcı adı zaten kullanılıyor.')
        return username
    
    def save(self, commit=True):
        staff = super().save(commit=False)
        
        # Kullanıcı hesabı oluştur veya güncelle
        if staff.user:
            # Güncelleme
            user = staff.user
            user.username = self.cleaned_data['username']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if self.cleaned_data.get('password'):
                user.set_password(self.cleaned_data['password'])
            user.save()
        else:
            # Yeni kullanıcı
            if not self.cleaned_data.get('password'):
                raise forms.ValidationError('Yeni personel için şifre gereklidir.')
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                role='staff'
            )
            staff.user = user
        
        if self.company:
            staff.company = self.company
        
        if commit:
            staff.save()
        
        return staff

