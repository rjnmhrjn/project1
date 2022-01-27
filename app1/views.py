from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    students = []
    return render(request, 'app1/home.html', {'names': students})

def about(request):
    return render(request, 'app1/about.html')