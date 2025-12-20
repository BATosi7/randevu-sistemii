from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="FontAwesome icon class", default="fa-solid fa-store")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Company(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='companies')
    name = models.CharField(max_length=200)
    address = models.TextField()
    description = models.TextField(blank=True)
    average_rating = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.company.name}"

class Staff(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='staff_members')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='staff_profile')
    name = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} - {self.company.name}"

class StaffAvailability(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Staff Availabilities"
        unique_together = ['staff', 'date', 'start_time']
    
    def __str__(self):
        return f"{self.staff.name} - {self.date} {self.start_time}-{self.end_time}"
