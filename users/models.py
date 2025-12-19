from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Müşteri'),
        ('business_owner', 'İşletme Sahibi'),
        ('admin', 'Yönetici'),
        ('staff', 'Personel'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
