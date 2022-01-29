from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

from .models import Book

# Create your views here.
ratings_data = pd.read_csv('./data/books.csv', on_bad_lines='skip')

def say_hello(request):
    qs = Book.objects.all()
    readers = [{'ISBN': x.isbn, 'Book-Title': x.title, 'Year-Of-Publication': x.year, 'Publisher': x.publisher} for x in qs]

    df = pd.DataFrame(readers)

    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d', data}

    return render(request, 'hello.html', context)