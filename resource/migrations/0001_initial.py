# Generated by Django 5.0 on 2024-08-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100, unique=True, verbose_name='主机名')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP地址')),
                ('operating_system', models.CharField(max_length=100, verbose_name='操作系统')),
                ('cpu_cores', models.IntegerField(verbose_name='CPU核心数')),
                ('memory_gb', models.FloatField(verbose_name='内存(GB)')),
                ('storage_gb', models.FloatField(verbose_name='存储(GB)')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
            },
        ),
    ]
