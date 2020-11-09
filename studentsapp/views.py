from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django import forms
from .forms import StudentForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def profile(request):

    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'profile.html', context)


# def profile(request):
#     # if request.method == 'GET':
#     #     return render(request, 'profile.html')
#     # else:
#     admission_no = request.POST['adm_number']
#     admission_date = request.POST['adm_date']
#     class_sec = request.POST['class_sec']
#     roll_no = request.POST['roll_no']
#     name = request.POST['st_name']
#     aadhar_no = request.POST['aad_no']
#     mother_name = request.POST['mother_name']
#     mother_aadhar = request.POST['mother_aad']
#     father_name = request.POST['father_name']
#     father_aadhar = request.POST['father_aad']
#     dob = request.POST['dob']
#     mobile_1 = request.POST['mob1']
#     mobile_2 = request.POST['mob2']
#     pr_addr = request.POST['pr_address']
#     pm_addr = request.POST['perm_address']
#     email_id = request.POST['email']
#     gender = request.POST['gender']
#     Feecategory = request.POST['fee_category']
#     caste = request.POST['caste']
#     blood_grp = request.POST['blood_grp']
#     Religion = request.POST['religion']
#     ref_admn_no = request.POST['ref_no']
#     action = request.POST['action']
#     arrear_due = request.POST['arrear_due']
#     ttod = request.POST['ttod']
#     ttnd = request.POST['tnd']
#     due = request.POST['due']
#     religions = Religion.objects.all()

#     ins = Student(admission_no=admission_no, admission_date=admission_date, class_sec=class_sec, roll_no=roll_no, name=name, aadhar_no=aadhar_no, mother_name=mother_name, mother_aadhar=mother_aadhar, father_name=father_name,
#                   father_aadhar=father_aadhar, dob=dob, mobile_1=mobile_1, mobile_2=mobile_2, pr_addr=pr_addr, pm_addr=pm_addr, email_id=email_id, gender=gender, Feecategory=Feecategory, caste=caste, blood_grp=blood_grp, Religion=Religion,
#                   ref_admn_no=ref_admn_no, action=action, arrear_due=arrear_due, ttod=ttod, ttnd=ttnd, due=due)
#     ins.save()
#     print("This is post")
#     return render(request, 'profile.html', {'religions': religions})


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
