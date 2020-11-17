# Generated by Django 3.1.2 on 2020-11-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0013_auto_20201118_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='blood_grp',
            field=models.CharField(blank=True, choices=[('AB+', 'AB+'), ('AB-', 'AB-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], default=None, max_length=5, null=True, verbose_name='Blood Group'),
        ),
    ]
