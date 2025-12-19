from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def login_success(request):
    """
    Redirects users based on their role after login.
    """
    if request.user.role == 'business_owner':
        return redirect('dashboard')
    return redirect('home')
