from django.shortcuts import render, redirect
import requests
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conf_pass = request.POST['conf_pass']
        if password != conf_pass:
            return render(request,'reg.html',{'pass_mismatch':'password not matching with confirm password'})
        u = User.objects.create_user(
            first_name=first_name,
            last_name = last_name,
            email= email,
            username= username,
            password=password
        )
        return redirect('login')
    return render(request, 'reg.html')
def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('home', pk=request.user.id) 
        else:
            return render(request, 'login.html', {'error':'Invalid User'})      
    return render(request, 'login.html')
@login_required(login_url='login')      
def logout_(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def profile(request):
    a = User.objects.get(username = request.user)
    return render(request, 'profile.html')
