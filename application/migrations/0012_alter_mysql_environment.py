# Generated by Django 5.0 on 2024-09-03 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_alter_mysql_environment'),
        ('common', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql',
            name='environment',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='common.environment', verbose_name='环境'),
        ),
    ]
