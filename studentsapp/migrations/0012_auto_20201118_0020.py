# Generated by Django 3.1.2 on 2020-11-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0011_auto_20201118_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='tc',
            field=models.CharField(blank=True, choices=[('ISSUED', 'Issued'), ('NOT ISSUED', 'Not Issued')], default=None, max_length=20, null=True, verbose_name='TC'),
        ),
    ]
