from django.contrib import admin
from .models import *
from .forms import StudentForm
# Register your models here.

class Classlist(admin.ModelAdmin):
    list_display = ['name']

class Studentlist(admin.ModelAdmin):
    list_display = ['name', 'class_sec', 'roll_no']
    form = StudentForm


admin.site.register(Class,Classlist)
admin.site.register(Gender)
admin.site.register(Fee_category)
admin.site.register(Caste)
admin.site.register(Religion)
admin.site.register(Student,Studentlist)
