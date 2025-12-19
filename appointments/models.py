from django.db import models
from django.conf import settings
from business.models import Company, Service, Staff

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Bekliyor'),
        ('confirmed', 'Onaylandı'),
        ('cancelled', 'İptal Edildi'),
        ('completed', 'Tamamlandı'),
        ('no_show', 'Gelmedi'),
    )

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.company.name} - {self.date} {self.time}"

class Rating(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='rating')
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    company = models.ForeignKey('business.Company', on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.company.name} - {self.score} stars"


class Review(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='review')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.appointment}"
