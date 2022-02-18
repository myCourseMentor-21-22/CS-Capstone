from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

from .models import Book

# Create your views here.

def say_hello(request):
    data = pd.read_excel('./data/CS210HW1.xlsx')
    context = {'d': data.to_html()}
    return render(request, 'hello.html', context)