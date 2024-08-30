# Generated by Django 5.0 on 2024-08-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='cpu_cores',
            field=models.IntegerField(default=8, verbose_name='CPU核心数'),
        ),
        migrations.AlterField(
            model_name='host',
            name='description',
            field=models.TextField(blank=True, default='description', verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(default='hostname', max_length=100, unique=True, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='host',
            name='ip_address',
            field=models.GenericIPAddressField(default='0.0.0.0', verbose_name='IP地址'),
        ),
        migrations.AlterField(
            model_name='host',
            name='memory_gb',
            field=models.FloatField(default=16.0, verbose_name='内存(GB)'),
        ),
        migrations.AlterField(
            model_name='host',
            name='operating_system',
            field=models.CharField(default='Unknown OS', max_length=100, verbose_name='操作系统'),
        ),
        migrations.AlterField(
            model_name='host',
            name='storage_gb',
            field=models.FloatField(default=256.0, verbose_name='存储(GB)'),
        ),
    ]
