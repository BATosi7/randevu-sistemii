from django.contrib import admin
from .models import Appointment, Review

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'company', 'service', 'staff', 'date', 'time', 'status')
    list_filter = ('status', 'date', 'company')
    search_fields = ('customer__username', 'company__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'rating', 'created_at')
    list_filter = ('rating',)
