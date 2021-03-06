from django.db import models
from django.contrib.auth.models import User
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
# Create your models here.


class Class(models.Model):  # Foreign key
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_Class():
        return Class.objects.all()

    def __str__(self):
        return self.name

    class Meta:
        # verbose_name = 'Class'
        verbose_name_plural = 'Classes'


class Gender(models.Model):  # Foreign key
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Fee_structure(models.Model):
    class_name = models.CharField(verbose_name="Class",max_length=40)
    subs_fee = models.IntegerField(verbose_name="Subsidiary Fee")
    lab_fee = models.IntegerField(verbose_name="Laboratory Fee")
    tut_fee = models.IntegerField(verbose_name="Tuition Fee")
    comp_fee = models.IntegerField(verbose_name="Computer Fee")
    one_time = models.IntegerField(verbose_name="OneTime Fee")
    normal = models.IntegerField(verbose_name="Normal Fee")

    class Meta:
        verbose_name = 'Fee structure'
        verbose_name_plural = 'Fee structure'

    def __str__(self):
        return "class "+self.class_name

class Fee_category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Fee category'
        verbose_name_plural = 'Fee categories'


class Caste(models.Model):  # Foreign key
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_castes():
        return Caste.objects.all()

    def __str__(self):
        return self.name


class Religion(models.Model):   # Foreign key
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_Religion():
        return Religion.objects.all()

    def __str__(self):
        return self.name

Due_Choices = (
    ("YES", "Yes"),
    ("NO", "No"),
)

Blood_grp = (
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    )

TC_Choices = (
    ("ISSUED", "Issued"),
    ("NOT ISSUED", "Not Issued"),
)


class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    admission_no = models.CharField(
        verbose_name="Admission Number", max_length=30, blank=True,null=True)  #
    admission_date = models.DateField(
        verbose_name="Admission Date", auto_now=False, auto_now_add=False, blank=True,null=True)
    class_sec = models.ForeignKey(
        Class, verbose_name="Class-Sec", blank=False, on_delete=models.CASCADE)   #
    roll_no = models.IntegerField(
        verbose_name="Roll No.",blank=True, null=True)  #
    name = models.CharField(verbose_name="Name", max_length=50, blank=False)
    aadhar_no = models.CharField(
        verbose_name="Aadhar No.", max_length=30, blank=True,null=True)
    mother_name = models.CharField(
        verbose_name="Mother's name", max_length=40, blank=True)
    mother_aadhar = models.CharField(
        verbose_name="Mother's Aadhar No.", max_length=30, blank=True,null=True)
    father_name = models.CharField(
        verbose_name="Father's Name", max_length=50, blank=True)
    father_aadhar = models.CharField(
        verbose_name="Father's Aadhar No.", max_length=30, blank=True,null=True)
    dob = models.DateField(verbose_name="D.O.B",
                           auto_now=False, auto_now_add=False, blank=True,null=True)
    mobile_1 = models.CharField(max_length=10, blank=True,null=True)
    mobile_2 = models.CharField(max_length=10, blank=True,null=True)
    pr_addr = models.CharField(
        verbose_name="Present Address", max_length=100, blank=True,null=True)
    pm_addr = models.CharField(
        verbose_name="Permanent Address", max_length=100, blank=True,null=True)
    email_id = models.EmailField(max_length=40, blank=True,null=True)
    gender = models.ForeignKey(Gender, blank=False, on_delete=models.CASCADE)
    Feecategory = models.CharField(max_length=30, blank=True,null=True)
    caste = models.ForeignKey(
        Caste, blank=True, null=True, on_delete=models.CASCADE)
    blood_grp = models.CharField(verbose_name="Blood Group",max_length=5,choices=Blood_grp,null=True, blank=True,default=None)
    Religion = models.ForeignKey(
        Religion,null=True, blank=True, on_delete=models.CASCADE)
    ref_admn_no = models.CharField(
        verbose_name="Reference admission no. of Ex-Student", max_length=30, blank=True, null=True)
    action = models.CharField(verbose_name="Action", max_length=10, blank=True,null=True)
    arrear_due = models.CharField(
        verbose_name="Arrear Due", max_length=10,null=True, blank=True)
    ttod = models.CharField(
        verbose_name="Total Onetime Due", max_length=10,null=True, blank=True)
    ttnd = models.CharField(
        verbose_name="Total Normal Due", max_length=10, null=True,blank=True)
    # due = models.BooleanField(
    #     verbose_name="Due(YES/NO)", blank=True, null=True, default=None)
    # tc = models.BooleanField(
    #     verbose_name="TC(YES/NO)", blank=True, null=True, default=None)
    due = models.CharField(
        verbose_name="Due(YES/NO)",max_length=10,choices=Due_Choices, blank=True, null=True, default=None)
    tc = models.CharField(
        verbose_name="TC",max_length=20,choices=TC_Choices, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        db_table = 'Student_table'

# class_sec,gender,caste,religion
