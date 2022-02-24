from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.

def index(request):
    return render(request, 'home.html')

def my_information(request):
    return render(request, 'info.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def testing(request):
    return render(request, 'testing.html')