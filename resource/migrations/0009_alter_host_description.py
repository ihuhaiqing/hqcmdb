# Generated by Django 5.0 on 2024-09-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0008_host_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='description',
            field=models.CharField(blank=True, default='description', max_length=255, verbose_name='描述'),
        ),
    ]
