from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/data/', views.dashboard_data, name='dashboard_data'),
    path('appointment/<int:pk>/status/<str:status>/', views.update_appointment_status, name='update_appointment_status'),
    # Staff URLs (Personel)
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/availability/add/', views.add_availability, name='add_availability'),
    # Staff Management URLs (İşletme Sahibi)
    path('staff/', views.manage_staff, name='manage_staff'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/<int:pk>/edit/', views.edit_staff, name='edit_staff'),
    path('staff/<int:pk>/delete/', views.delete_staff, name='delete_staff'),
]
