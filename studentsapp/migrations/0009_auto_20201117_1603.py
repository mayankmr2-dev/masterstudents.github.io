# Generated by Django 3.1.2 on 2020-11-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0008_auto_20201116_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='D.O.B'),
        ),
    ]
