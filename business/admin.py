from django.contrib import admin
from .models import Category, Company, Service, Staff

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'owner', 'average_rating')
    list_filter = ('category',)
    search_fields = ('name', 'owner__username')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'duration', 'price')
    list_filter = ('company',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'expertise')
    list_filter = ('company',)
