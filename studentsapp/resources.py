from import_export import resources
from import_export import fields, resources
from .models import *
from import_export.widgets import ForeignKeyWidget,DateWidget,BooleanWidget


class StudentResource(resources.ModelResource):
    id = fields.Field(attribute='id',column_name='id')
    admission_no = fields.Field(attribute='admission_no',column_name='admission_no')
    admission_date = fields.Field(attribute='admission_date',column_name='admission_date',widget=DateWidget())
    class_sec = fields.Field(attribute='class_sec',column_name='class_sec',widget=ForeignKeyWidget(Class, 'name'))
    roll_no = fields.Field(attribute='roll_no',column_name='roll_no')
    name = fields.Field(attribute='name',column_name='name')
    aadhar_no = fields.Field(attribute='aadhar_no',column_name='aadhar_no')
    mother_name = fields.Field(attribute='mother_name',column_name='mother_name')
    mother_aadhar = fields.Field(attribute='mother_aadhar',column_name='mother_aadhar')
    father_name = fields.Field(attribute='father_name',column_name='father_name')
    father_aadhar = fields.Field(attribute='father_aadhar',column_name='father_aadhar')
    dob = fields.Field(attribute='dob',column_name='dob',widget=DateWidget())
    mobile_1 = fields.Field(attribute='mobile_1',column_name='mobile_1')
    mobile_2 = fields.Field(attribute='mobile_2',column_name='mobile_2')
    pr_addr = fields.Field(attribute='pr_addr',column_name='pr_addr')
    pm_addr = fields.Field(attribute='pm_addr',column_name='pm_addr')
    email_id = fields.Field(attribute='email_id',column_name='email_id')
    gender = fields.Field(attribute='gender',column_name='gender',widget=ForeignKeyWidget(Gender, 'name'))
    Feecategory = fields.Field(attribute='Feecategory',column_name='Feecategory')
    caste = fields.Field(attribute='caste',column_name='caste',widget=ForeignKeyWidget(Caste, 'name'))
    blood_grp = fields.Field(attribute='blood_grp',column_name='blood_grp')
    Religion = fields.Field(attribute='Religion',column_name='Religion',widget=ForeignKeyWidget(Religion, 'name'))
    ref_admn_no = fields.Field(attribute='ref_admn_no',column_name='ref_admn_no')
    action = fields.Field(attribute='action',column_name='action')
    arrear_due = fields.Field(attribute='arrear_due',column_name='arrear_due')
    ttod = fields.Field(attribute='ttod',column_name='ttod')
    ttnd = fields.Field(attribute='ttnd',column_name='ttnd')
    due = fields.Field(attribute='due',column_name='due')
    tc = fields.Field(attribute='tc',column_name='tc')
    
    class Meta:
        model = Student
        # fields = ('id','admission_no', 'admission_date', 'class_sec__name', 'roll_no', 'name', 'aadhar_no', 'mother_name', 'mother_aadhar', 'father_name',
        #           'father_aadhar', 'dob', 'mobile_1', 'mobile_2', 'pr_addr', 'pm_addr', 'email_id', 'gender__name', 'Feecategory', 'caste__name', 'blood_grp', 'Religion__name',
        #           'ref_admn_no', 'action', 'arrear_due', 'ttod', 'ttnd', 'due','tc')
