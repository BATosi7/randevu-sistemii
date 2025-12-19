from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/data/', views.dashboard_data, name='dashboard_data'),
    path('appointment/<int:pk>/update/<str:status>/', views.update_appointment_status, name='update_appointment_status'),
]
