from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


def home(request):
    return render(request, 'home.html')


def profile(request):
    if request.method == 'POST':
        print("This is post")

    return render(request, 'profile.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def table(request):
    return render(request, 'table.html')


def feestructure(request):
    return render(request, 'feestructure.html')


def classfee(request):
    return render(request, 'classfee.html')
