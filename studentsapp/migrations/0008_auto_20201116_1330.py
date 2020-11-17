# Generated by Django 3.1.2 on 2020-11-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0007_auto_20201116_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee_structure',
            name='comp_fee',
            field=models.IntegerField(verbose_name='Computer Fee'),
        ),
        migrations.AlterField(
            model_name='fee_structure',
            name='lab_fee',
            field=models.IntegerField(verbose_name='Laboratory Fee'),
        ),
        migrations.AlterField(
            model_name='fee_structure',
            name='normal',
            field=models.IntegerField(verbose_name='Normal Fee'),
        ),
        migrations.AlterField(
            model_name='fee_structure',
            name='one_time',
            field=models.IntegerField(verbose_name='OneTime Fee'),
        ),
        migrations.AlterField(
            model_name='fee_structure',
            name='subs_fee',
            field=models.IntegerField(verbose_name='Subsidiary Fee'),
        ),
        migrations.AlterField(
            model_name='fee_structure',
            name='tut_fee',
            field=models.IntegerField(verbose_name='Tuition Fee'),
        ),
    ]