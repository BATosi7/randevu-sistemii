from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from business.models import Service

@login_required
def create_appointment(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    company = service.company

    # Prevent business owners and staff from booking appointments
    if request.user.role in ['business_owner', 'staff']:
        messages.error(request, 'İşletme sahipleri ve personel randevu alamaz. Sadece müşteriler randevu alabilir.')
        return redirect('company_detail', pk=company.id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, company=company)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.customer = request.user
            appointment.company = company
            appointment.service = service  # Service from URL
            appointment.save()
            messages.success(request, f'Randevunuz başarıyla oluşturuldu! {company.name} - {appointment.service.name} ({appointment.date.strftime("%d.%m.%Y")} - {appointment.time})')
            return redirect('my_appointments')
    else:
        form = AppointmentForm(company=company, initial={'service': service})

    return render(request, 'appointments/create_appointment.html', {
        'form': form,
        'service': service,
        'company': company
    })

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(customer=request.user).order_by('-date', '-time')
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})

@login_required
def cancel_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, customer=request.user)
    if appointment.status in ['pending', 'confirmed']:
        appointment.status = 'cancelled'
        appointment.save()
    return redirect('my_appointments')

@login_required
def rate_appointment(request, pk):
    from .models import Rating
    from .forms import RatingForm
    
    appointment = get_object_or_404(Appointment, pk=pk, customer=request.user)
    
    # Validations
    if appointment.status != 'completed':
        messages.error(request, 'Sadece tamamlanan randevuları değerlendirebilirsiniz.')
        return redirect('my_appointments')
    
    if hasattr(appointment, 'rating'):
        messages.error(request, 'Bu randevuyu zaten değerlendirdiniz.')
        return redirect('my_appointments')
    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.appointment = appointment
            rating.customer = request.user
            rating.company = appointment.company
            rating.save()
            
            # Update company average rating
            update_company_rating(appointment.company)
            
            messages.success(request, 'Değerlendirmeniz kaydedildi. Teşekkür ederiz!')
            return redirect('my_appointments')
    else:
        form = RatingForm()
    
    return render(request, 'appointments/rate_appointment.html', {
        'form': form,
        'appointment': appointment
    })

def update_company_rating(company):
    from django.db.models import Avg
    from .models import Rating
    
    avg_rating = Rating.objects.filter(company=company).aggregate(Avg('score'))['score__avg']
    if avg_rating:
        company.average_rating = round(avg_rating, 1)
        company.save()
