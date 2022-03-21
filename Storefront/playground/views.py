
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from .forms import PostCredentials, PostForm, PostUser

import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.
name_cookie = ""


def index(request):
    return render(request, 'home.html')

def my_information(request):
    data = Student.objects.get(stu_id=1)  
    name_cookie = str(data)
    sid = str(Student.objects.get(name="John Doe"))
    return render(request, 'info.html', {"name":name_cookie[2:], "stu_id":sid[:1]} )

@csrf_exempt
def log(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate( request, username=User.objects.get(email=email), password=password)
       
        if user is not None:      
            login(request, user)
            return redirect('/playground')
        else:
            return redirect('register')
    
    return render(request,'login.html')

def edit(request):
    s = str(Student.objects.get(name=name_cookie))[2:]
    return render(request, 'edit.html', {"name":s})

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email)
        user.set_password(password)
        user.save()
        return redirect("/playground")


    return render(request, 'register.html')

def logout_view(request):
    logout(request)

def testing(request):
    return render(request, 'testing.html')