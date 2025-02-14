from enum import auto
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect ('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
        

    return render(request,'login.html')




# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        phone=request.POST.get("phone")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        email=request.POST.get("email")

        if password1 == password2:
            if User.objects.filter(username=username).exists(): 
                messages.info(request,'user taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                user.save()
                messages.info(request,'user created')
                return redirect('/')
        else:
            messages.info(request,'password does not match')
            return redirect('register')
    return render(request,"register.html")

def logout_view(request):
    logout(request)
    return redirect('/')