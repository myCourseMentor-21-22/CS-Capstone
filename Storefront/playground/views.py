
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
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
    name = request.user.first_name + " " + request.user.last_name
    email = request.user.email
    username = request.user.username
    return render(request, 'info.html', {"name":name, "email":email, "username":username} )

@csrf_exempt
def log(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email)
        except:
            username = "None"
        user = authenticate( request, username=username, password=password)
       
        if user is not None:      
            login(request, user)
            return redirect('/playground')
        else:
            message="Username/Password is Wrong"
            return render(request, 'login.html', {"message":message})
    
    return render(request,'login.html')

def edit(request):
    if request.method == "POST":
        password = request.POST['password']
        request.user.set_password(password)
        request.user.save()
        return redirect('index')

    return render(request, 'edit.html')

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
    return redirect('log')

def testing(request):
    return render(request, 'testing.html')