# Generated by Django 5.0 on 2024-08-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatingsystem',
            name='name',
            field=models.CharField(default='Red Hat Enterprise Linux', max_length=100, verbose_name='名称'),
        ),
    ]
