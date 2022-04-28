
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

from .models import GradeData

import pandas as pd
import matplotlib.pyplot as plt
import logging

# Create your views here.
name_cookie = ""


def index(request):
    if (request.user.is_authenticated):
        id = request.user.id
        stuData = GradeData.objects.get(studentId=id)

        cs101=stuData.cs101
        cs102=stuData.cs102
        cs140 = stuData.cs140
        mth120=stuData.mth120
        hw1=stuData.hw1
        test1=stuData.test1
        hw2=stuData.hw3
        test2=stuData.test2
        final=stuData.final

        nextAssignment = ''
        if cs101 == '':
            recorded_grades['cs101']
            nextAssignment='cs101'
        elif cs102 == '':
            nextAssignment='cs102'
        elif cs140=='':
            nextAssignment='cs140'
        elif mth120=='':
            nextAssignment='mth120'
        elif hw1=='':
            nextAssignment='hw1'
        elif test1=='':
            nextAssignment='test 1'
        elif hw2=='':
            nextAssignment='hw2'
        elif test2=='':
            nextAssignment='test 2'
        elif final == '':
            nextAssignment = 'final'
            
        pred_next = pred_code.pred_next(cs101,cs102,cs140,mth120,hw1,test1,hw2,test2,final)
        pred_final = pred_code.predict_final(cs101,cs102,cs140,mth120,hw1,test1,hw2,test2,final)

        data = {
            'name': request.user,
            'id': request.user.id,
            'recorded_grades':
            {'cs101': cs101,
                'cs102': cs102,
                'cs140': cs140,
                'mth120': mth120,
                'hw1': hw1,
                'test1': test1,
                'hw2': hw2,
                'test2': test2,
                'final': final
            },
            'next_assignment': nextAssignment,
            'pred_next': pred_next,
            'pred_final': pred_final
        }

        return render(request, 'dashboard.html', data)
    else:
        return render(request, 'register.html')

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

        login(request, user)

        gradeData = GradeData(studentId=user.id, cs101=request.POST["grade1"], cs102=request.POST["grade2"], cs140=request.POST["grade3"],
        mth120=request.POST["grade4"], hw1=request.POST["grade5"], test1=request.POST["grade6"], hw3=request.POST["grade7"], test2=request.POST["grade8"], 
        final=request.POST["grade9"])
        gradeData.save()
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