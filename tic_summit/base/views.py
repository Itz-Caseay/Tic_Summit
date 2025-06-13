from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  authenticate
from django.contrib import messages
from .models import User

# Create your views here.

def home(request):
    return render(request, "base/home.html")

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "invalid credentials")
                return redirect('login_user')
        except Exception as e:
            messages.error(request, {'error':e})
        
    return render(request, "base/login.html")

def logout_user(request):
    logout(request)
    return redirect('home')

def signup(request):
    
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            
            if password == password2:
                if User.objects.filter(email=email, username=username).exists():
                    messages.error(request, 'email or username already in use')
                    return redirect('signup')
                
                else:
                    user=User.objects.create_user(username=username, email=email, password=password)
                    
                    login(request, user)
                    messages.success(request, 'account created')
                    return redirect('home')
            
            else:
                messages.error(request, 'Password does not match')
                return redirect('signup')
    except (ValueError or Exception) as e:
            messages.error(request, e)
            return redirect('signup')
    
    return render(request, "base/signup.html")
