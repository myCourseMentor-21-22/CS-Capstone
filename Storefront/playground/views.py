
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from playground.testing import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from .forms import PostCredentials, PostForm, PostUser, PredictPriorForm
from data import Final_Capstone_Prediction_Code2 as pred_code

import pandas as pd
import matplotlib.pyplot as plt
import logging

# Create your views here.
name_cookie = ""


def index(request):
    return render(request, 'home.html')

def my_information(request):
    # Getting the name of the logged in user. Right now prints the username.
    # TODO: We'll wanna somehow get the actual name of the person later.
    return render(request, 'info.html', {'name':request.user, 'stu_id':request.user.id})

def predict_prior(request):
    ctx={}
    if (request.method == "POST"):
        cs101=request.POST['grade1']
        cs102 = request.POST['grade2']
        cs103=request.POST['grade3']
        mth120 = request.POST['grade4']
        result = pred_code.pred_prior(cs101,cs102,cs103,mth120)
        ctx = {'result' : result}

    return render(request, "predict_prior.html", ctx)

def predict_next(request):
    ctx={}
    if (request.method == "POST"):
        cs101=request.POST['grade1']
        cs102 = request.POST['grade2']
        cs103=request.POST['grade3']
        mth120 = request.POST['grade4']
        g5 = request.POST['grade5']
        g6 = request.POST['grade6']
        g7 = request.POST['grade7']
        g8 = request.POST['grade8']
        g9 = request.POST['grade9']
        result = pred_code.pred_next(cs101,cs102,cs103,mth120, g5, g6, g7, g8, g9)
        ctx = {'result' : result}

    return render(request, "predict_next.html", ctx)

def predict_final(request):
    ctx={}
    if (request.method == "POST"):
        cs101=request.POST['grade1']
        cs102 = request.POST['grade2']
        cs103=request.POST['grade3']
        mth120 = request.POST['grade4']
        g5 = request.POST['grade5']
        g6 = request.POST['grade6']
        g7 = request.POST['grade7']
        g8 = request.POST['grade8']
        g9 = request.POST['grade9']
        result = pred_code.predict_final(cs101,cs102,cs103,mth120, g5, g6, g7, g8, g9)
        ctx = {'result' : result}

    return render(request, "predict_final.html", ctx)

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
            return redirect('/register')
    
    return render(request,'login.html')

def info(request):
    s = str(Student.objects.get(name=name_cookie))[2:]
    return render(request, 'info.html', {'name':s})

def edit(request):
    #s = str(Student.objects.get(name=name_cookie))[2:]
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

def display_grades(request):
    context = {
        'data': 
        [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
        ]}

    return render(request, 'testing.html', context)
def logout_view(request):
    logout(request)

def testing(request):
    return render(request, 'testing.html')