from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django import forms
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login')
def profile(request):

    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'profile.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

@login_required(login_url='/login')
def table(request):
    return render(request, 'table.html')

@login_required(login_url='/login')
def feestructure(request):
    return render(request, 'feestructure.html')

@login_required(login_url='/login')
def classfee(request):
    return render(request, 'classfee.html')
