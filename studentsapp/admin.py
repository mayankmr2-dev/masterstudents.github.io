from django.contrib import admin
from .models import *
from .forms import StudentForm
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .resources import StudentResource

# Register your models here.

# class StudentResource(resources.ModelResource):
#     class Meta:
#         model = Student

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ['id','name', 'class_sec', 'roll_no']
    form = StudentForm
    pass

class Classlist(admin.ModelAdmin):
    list_display = ['name']

class Feestructurelist(admin.ModelAdmin):
    list_display = ["class_name","subs_fee",'lab_fee','tut_fee','comp_fee','one_time','normal']

# class Studentlist(admin.ModelAdmin):


admin.site.site_header = "DEMS Admin"
admin.site.site_title = "DEMS Admin Portal"
admin.site.index_title = "Welcome to DEMS Portal"
admin.site.register(Class,Classlist)
admin.site.register(Gender)
admin.site.register(Fee_structure,Feestructurelist)
admin.site.register(Fee_category)
admin.site.register(Caste)
admin.site.register(Religion)
# admin.site.register(Student,Studentlist)
