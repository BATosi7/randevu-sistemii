from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Q
import datetime
from .models import Category, Company, StaffAvailability, Staff, Service
from appointments.models import Appointment

def home(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        companies = Company.objects.filter(category_id=category_id)
    else:
        companies = Company.objects.all()[:6]
        
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
    
    appointments = Appointment.objects.filter(company=company).order_by('date', 'time')
    
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
    
    labels = []
    data = []
    today = timezone.now().date()
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        count = Appointment.objects.filter(company=company, date=date).count()
        labels.append(date.strftime("%d %b"))
        data.append(count)
    
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
        
        status_messages = {
            'confirmed': f'Randevu onaylandı: {appointment.customer.username} - {appointment.service.name}',
            'cancelled': f'Randevu reddedildi: {appointment.customer.username} - {appointment.service.name}',
            'completed': f'Randevu tamamlandı olarak işaretlendi: {appointment.customer.username} - {appointment.service.name}',
            'no_show': f'Randevu "Gelmedi" olarak işaretlendi: {appointment.customer.username} - {appointment.service.name}',
        }
        
        if status in status_messages:
            messages.success(request, status_messages[status])
    
    return redirect('dashboard')

# Personel Views
def is_staff(user):
    return user.is_authenticated and user.role == 'staff' and hasattr(user, 'staff_profile')

@user_passes_test(is_staff)
def staff_dashboard(request):
    """Personel dashboard'u"""
    staff_profile = request.user.staff_profile
    today = timezone.now().date()
    
    appointments = Appointment.objects.filter(
        staff=staff_profile
    ).order_by('date', 'time')
    
    availabilities = StaffAvailability.objects.filter(
        staff=staff_profile,
        date__gte=today
    ).order_by('date', 'start_time')
    
    today_appointments = appointments.filter(date=today).count()
    pending_appointments = appointments.filter(status='pending').count()
    completed_appointments = appointments.filter(status='completed').count()
    
    context = {
        'staff': staff_profile,
        'appointments': appointments,
        'availabilities': availabilities,
        'today_appointments': today_appointments,
        'pending_appointments': pending_appointments,
        'completed_appointments': completed_appointments,
    }
    return render(request, 'business/staff_dashboard.html', context)

@user_passes_test(is_staff)
def add_availability(request):
    """Personel müsait saat ekler"""
    from .forms import AvailabilityForm
    
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.staff = request.user.staff_profile
            availability.save()
            messages.success(request, 'Müsait saat eklendi.')
            return redirect('staff_dashboard')
    else:
        form = AvailabilityForm()
    
    return render(request, 'business/add_availability.html', {'form': form})

# Personel Yönetimi (İşletme Sahibi)
@user_passes_test(is_business_owner)
def manage_staff(request):
    """Personel listesi"""
    company = request.user.company
    staff_members = Staff.objects.filter(company=company)
    
    return render(request, 'business/manage_staff.html', {
        'staff_members': staff_members
    })

@user_passes_test(is_business_owner)
def add_staff(request):
    """Personel ekle"""
    from .forms import StaffForm
    company = request.user.company
    
    if request.method == 'POST':
        form = StaffForm(request.POST, company=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personel başarıyla eklendi.')
            return redirect('manage_staff')
    else:
        form = StaffForm(company=company)
    
    return render(request, 'business/staff_form.html', {
        'form': form,
        'title': 'Personel Ekle'
    })

@user_passes_test(is_business_owner)
def edit_staff(request, pk):
    """Personel düzenle"""
    company = request.user.company
    from .forms import StaffForm
    staff = get_object_or_404(Staff, pk=pk, company=company)
    
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff, company=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personel bilgileri güncellendi.')
            return redirect('manage_staff')
    else:
        form = StaffForm(instance=staff, company=company)
    
    return render(request, 'business/staff_form.html', {
        'form': form,
        'title': 'Personel Düzenle',
        'staff': staff
    })

@user_passes_test(is_business_owner)
def delete_staff(request, pk):
    """Personel sil"""
    company = request.user.company
    staff = get_object_or_404(Staff, pk=pk, company=company)
    
    if request.method == 'POST':
        # Kullanıcı hesabını da sil
        if staff.user:
            staff.user.delete()
        staff.delete()
        messages.success(request, 'Personel silindi.')
        return redirect('manage_staff')
    
    return render(request, 'business/staff_confirm_delete.html', {
        'staff': staff
    })


# Hizmet Yönetimi (İşletme Sahibi)
@user_passes_test(is_business_owner)
def manage_services(request):
    company = request.user.company
    services = Service.objects.filter(company=company)
    return render(request, 'business/manage_services.html', {'services': services})

@user_passes_test(is_business_owner)
def add_service(request):
    from .forms import ServiceForm
    company = request.user.company
    if request.method == 'POST':
        form = ServiceForm(request.POST, company=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hizmet başarıyla eklendi.')
            return redirect('manage_services')
    else:
        form = ServiceForm(company=company)
    return render(request, 'business/service_form.html', {'form': form, 'title': 'Hizmet Ekle'})

@user_passes_test(is_business_owner)
def edit_service(request, pk):
    from .forms import ServiceForm
    company = request.user.company
    service = get_object_or_404(Service, pk=pk, company=company)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service, company=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hizmet bilgileri güncellendi.')
            return redirect('manage_services')
    else:
        form = ServiceForm(instance=service, company=company)
    return render(request, 'business/service_form.html', {'form': form, 'title': 'Hizmet Düzenle', 'service': service})

@user_passes_test(is_business_owner)
def delete_service(request, pk):
    company = request.user.company
    service = get_object_or_404(Service, pk=pk, company=company)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Hizmet silindi.')
        return redirect('manage_services')
    return render(request, 'business/service_confirm_delete.html', {'service': service})
