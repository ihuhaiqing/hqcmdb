# Generated by Django 5.0 on 2024-09-03 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_mysql_database_name_alter_mysql_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysql',
            name='database_name',
        ),
    ]
