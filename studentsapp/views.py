from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import *
from django import forms
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Student,Caste
# Create your views here.

@login_required(login_url='/login')
def home(request):
    gen = Student.objects.filter(caste=6).count()
    obc = Student.objects.filter(caste=7).count()
    sc = Student.objects.filter(caste=8).count()
    st = Student.objects.filter(caste=9).count()
    context = {
        "gen":gen,"obc":obc,"sc":sc,"st":st
    }
    return render(request, 'home.html',context)


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

def profile_edit(request, id=None):
    instance = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('table')
    context = {
        'instance': instance,
        'form': form
    }
    return render(request, 'profile.html', context)

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

# @login_required(login_url='/login')
def table(request):
    student = Student.objects.all()
    # print(student)  
    context = {
        "student":student
    }
    return render(request, 'table.html', context)

def lis(request):
    student = Student.objects.all()
    # print(student)  
    context = {
        "student":student
    }
    return render(request, 'list.html', context)

def tc(request):
    student = Student.objects.filter(tc="ISSUED")
    # print(student)  
    context = {
        "student":student
    }
    return render(request, 'tc.html', context)

@login_required(login_url='/login')
def feestructure(request):
    return render(request, 'feestructure.html')

@login_required(login_url='/login')
def classfee(request):
    return render(request, 'classfee.html')

def profile_delete(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    instance.delete()
    return redirect("table")