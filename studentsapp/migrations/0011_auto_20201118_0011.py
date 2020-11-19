# Generated by Django 3.1.2 on 2020-11-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0010_auto_20201117_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='due',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], default=None, max_length=10, null=True, verbose_name='Due(YES/NO)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tc',
            field=models.BooleanField(blank=True, choices=[('ISSUED', 'Issued'), ('NOT ISSUED', 'Not Issued')], default=None, max_length=20, null=True, verbose_name='TC'),
        ),
    ]