# Generated by Django 5.0 on 2024-09-03 02:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_mysql_database_name'),
        ('common', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql',
            name='environment',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='common.environment', verbose_name='环境'),
        ),
    ]
