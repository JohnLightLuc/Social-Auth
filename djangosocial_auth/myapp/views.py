from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests, 'pages/index.html')

def login(requests):
    return render(requests, 'pages/login.html')