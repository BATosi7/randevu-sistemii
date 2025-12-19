from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Q
import datetime
from .models import Category, Company
from appointments.models import Appointment

def home(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        companies = Company.objects.filter(category_id=category_id)
    else:
        companies = Company.objects.all()[:6] # Show first 6 companies if no filter
        
    return render(request, 'business/home.html', {'categories': categories, 'companies': companies})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    services = company.services.all()
    staff_members = company.staff_members.all()
    return render(request, 'business/company_detail.html', {
        'company': company,
        'services': services,
        'staff_members': staff_members
    })

def is_business_owner(user):
    return user.is_authenticated and user.role == 'business_owner' and hasattr(user, 'company')

@user_passes_test(is_business_owner)
def dashboard(request):
    company = request.user.company
    today = timezone.now().date()
    
    # Check if we need to filter by status or date
    appointments = Appointment.objects.filter(company=company).order_by('date', 'time')
    
    # Stats
    pending_count = appointments.filter(status='pending').count()
    today_count = appointments.filter(date=today).count()
    completed_appointments = appointments.filter(status='completed')
    completed_count = completed_appointments.count()
    
    revenue = sum(appt.service.price for appt in completed_appointments)

    return render(request, 'business/dashboard.html', {
        'appointments': appointments,
        'pending_count': pending_count,
        'today_count': today_count,
        'completed_count': completed_count,
        'revenue': revenue
    })

@user_passes_test(is_business_owner)
def dashboard_data(request):
    company = request.user.company
    
    # 1. Weekly Appointment Trend (Last 7 days)
    labels = []
    data = []
    today = timezone.now().date()
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        count = Appointment.objects.filter(company=company, date=date).count()
        labels.append(date.strftime("%d %b"))
        data.append(count)
    
    # 2. Service Distribution
    service_data = Appointment.objects.filter(company=company).values('service__name').annotate(total=Count('id'))
    service_labels = [item['service__name'] for item in service_data]
    service_counts = [item['total'] for item in service_data]

    return JsonResponse({
        'weekly_labels': labels,
        'weekly_data': data,
        'service_labels': service_labels,
        'service_data': service_counts,
    })

@user_passes_test(is_business_owner)
def update_appointment_status(request, pk, status):
    appointment = get_object_or_404(Appointment, pk=pk, company=request.user.company)
    if status in dict(Appointment.STATUS_CHOICES):
        old_status = appointment.get_status_display()
        appointment.status = status
        appointment.save()
        
        # Status-specific messages
        status_messages = {
            'confirmed': f'Randevu onaylandı: {appointment.customer.username} - {appointment.service.name}',
            'cancelled': f'Randevu reddedildi: {appointment.customer.username} - {appointment.service.name}',
            'completed': f'Randevu tamamlandı olarak işaretlendi: {appointment.customer.username} - {appointment.service.name}',
            'no_show': f'Müşteri gelmedi olarak işaretlendi: {appointment.customer.username} - {appointment.service.name}',
        }
        
        if status in status_messages:
            messages.success(request, status_messages[status])
    
    return redirect('dashboard')
