from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='İsteğe bağlı')
    last_name = forms.CharField(max_length=30, required=True, help_text='İsteğe bağlı')
    email = forms.EmailField(max_length=254, help_text='Geçerli bir e-posta adresi girin.')
    phone = forms.CharField(max_length=15, required=False, label="Telefon Numarası")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'customer'  # Force role to customer
        if commit:
            user.save()
        return user
