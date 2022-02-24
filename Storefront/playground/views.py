from django.shortcuts import render
from django.http import HttpResponse
from playground.testing import *

import pandas as pd
import matplotlib.pyplot as plt
import logging

# Create your views here.

def index(request):
    return render(request, 'home.html')

def my_information(request):
    return render(request, 'info.html')

def login(request):
    return render(request, 'login.html')

def register(request):
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