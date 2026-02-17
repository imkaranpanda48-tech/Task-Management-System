from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('admin-dashboard')
            return redirect('employee-dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


