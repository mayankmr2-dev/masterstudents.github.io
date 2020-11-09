from django.db import models
from django.contrib.auth.models import User

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


class Student(models.Model):
    admission_no = models.CharField(
        verbose_name="Admission Number", max_length=30, blank=False)  #
    admission_date = models.DateField(
        verbose_name="Admission Date", auto_now=False, auto_now_add=False, blank=True,null=True)
    class_sec = models.ForeignKey(
        Class, verbose_name="Class-Sec", blank=False, on_delete=models.CASCADE)   #
    roll_no = models.IntegerField(
        verbose_name="Roll No.", default=False, blank=False, null=False)  #
    name = models.CharField(verbose_name="Name", max_length=50, blank=False)
    aadhar_no = models.CharField(
        verbose_name="Aadhar No.", max_length=30, blank=True)
    mother_name = models.CharField(
        verbose_name="Mother's name", max_length=40, blank=True)
    mother_aadhar = models.CharField(
        verbose_name="Mother's Aadhar No.", max_length=30, blank=True)
    father_name = models.CharField(
        verbose_name="Father's Name", max_length=50, blank=True)
    father_aadhar = models.CharField(
        verbose_name="Father's Aadhar No.", max_length=30, blank=True)
    dob = models.DateField(verbose_name="D.O.B",
                           auto_now=False, auto_now_add=False, blank=False)
    mobile_1 = models.CharField(max_length=10, blank=True)
    mobile_2 = models.CharField(max_length=10, blank=True)
    pr_addr = models.CharField(
        verbose_name="Present Address", max_length=100, blank=True)
    pm_addr = models.CharField(
        verbose_name="Permanent Address", max_length=100, blank=True)
    email_id = models.EmailField(max_length=40, blank=True)
    gender = models.ForeignKey(Gender, blank=False, on_delete=models.CASCADE)
    Feecategory = models.CharField(max_length=30, blank=True)
    caste = models.ForeignKey(
        Caste, blank=True, null=True, on_delete=models.CASCADE)
    blood_grp = models.CharField(max_length=5,null=True, blank=True)
    Religion = models.ForeignKey(
        Religion,null=True, blank=True, on_delete=models.CASCADE)
    ref_admn_no = models.CharField(
        verbose_name="Reference admission no. of Ex-Student", max_length=30, blank=True, null=True)
    action = models.CharField(verbose_name="Action", max_length=10, blank=True)
    arrear_due = models.CharField(
        verbose_name="Arrear Due", max_length=10,null=True, blank=True)
    ttod = models.CharField(
        verbose_name="Total Onetime Due", max_length=10,null=True, blank=True)
    ttnd = models.CharField(
        verbose_name="Total Normal Due", max_length=10, null=True,blank=True)
    due = models.BooleanField(
        verbose_name="Due(YES/NO)", blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        db_table = 'Student_table'
