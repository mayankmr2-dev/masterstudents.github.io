from django.forms import ModelForm
from .models import Student,Class,Caste,Religion,Gender
from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import FileExtensionValidator

# class RegistrationForm(UserCreationForm):
#     email 

class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False,validators=[FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")


class StudentForm(forms.ModelForm):
    class_sec = forms.ModelChoiceField(
        queryset=Class.objects.all(), initial=None)
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), initial=None)
    caste = forms.ModelChoiceField(queryset=Caste.objects.all(), initial=None)
    Religion = forms.ModelChoiceField(
        queryset=Religion.objects.all(), initial=None)

    class Meta(object):
        model = Student
        fields = ['admission_no', 'admission_date', 'class_sec', 'roll_no', 'name', 'aadhar_no', 'mother_name', 'mother_aadhar', 'father_name',
                  'father_aadhar', 'dob', 'mobile_1', 'mobile_2', 'pr_addr', 'pm_addr', 'email_id', 'gender', 'Feecategory', 'caste', 'blood_grp', 'Religion',
                  'ref_admn_no', 'action', 'arrear_due', 'ttod', 'ttnd', 'due','tc']
