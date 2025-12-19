from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:service_id>/', views.create_appointment, name='create_appointment'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('cancel/<int:pk>/', views.cancel_appointment, name='cancel_appointment'),
    path('rate/<int:pk>/', views.rate_appointment, name='rate_appointment'),
]
