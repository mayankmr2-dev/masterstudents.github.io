from django.db import models

# Create your models here.


class Class (models.Model):  # Foreign key
    name = models.Charfield(max_length=20)

    def __str__(self):
        return self.name

class Gender(models.Model): # Foreign key
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Fee_category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Caste(models.Model):  # Foreign key
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Religion(models.Model):   # Foreign key
    name = models.Charfield(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    admission_no = models.CharField(verbose_name="Admission Name",max_length=30,blank=False)  #
    admission_date = models.DateField(verbose_name="Admission Date",auto_now=False,auto_now_add=False,blank=True)
    class_sec = models.ForeignKey(Class,verbose_name="Class-Sec",blank=False)   #
    roll_no = models.IntegerField(verbose_name="Roll No.",default=False,blank=False,null=False)  #
    name = models.CharField(verbose_name="Name",max_length=50,blank=False) #
    aadhar_no = models.CharField(verbose_name="Aadhar No.",max_length=30,blank=True)
    mother_name = models.CharField(verbose_name="Mother's name",max_length=40,blank=True)
    mother_aadhar = models.CharField(verbose_name="Mother's Aadhar No.",max_length=30,blank=True)
    father_name = models.CharField(verbose_name="Father's Name",max_length=50,blank=True)
    father_aadhar = models.CharField(verbose_name="Father's Aadhar No.",max_length=30,blank=True)
    dob = models.CharField(verbose_name="D.O.B",auto_now=False,auto_now_add=False,blank=False)
    mobile_1 = models.CharField(max_length=10,blank=True)
    mobile_2 = models.CharField(max_length=10,blank=True)
    pr_addr = models.CharField(verbose_name="Present Address",max_length=100,blank=True)
    pm_addr = models.CharField(verbose_name="Permanent Address",max_length=100,blank=True)
    email_id = models.EmailField(max_length=40,blank=True)
    gender = models.ForeignKey(Gender,blank=False)
    Feecategory = models.CharField(max_length=30,blank=True)





