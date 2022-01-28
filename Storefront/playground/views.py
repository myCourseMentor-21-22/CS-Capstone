from csv import reader
from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# Create your views here.
ratings_data = pd.read_csv('./data/books.csv', on_bad_lines='skip')

def say_hello(request):
    return render(request, 'hello.html', {'name': ratings_data})