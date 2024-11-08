# Generated by Django 5.0 on 2024-08-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_environment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Project', max_length=100, unique=True, verbose_name='项目名称')),
                ('status', models.CharField(choices=[('online', '在线'), ('offline', '下线')], default='online', max_length=7, verbose_name='状态')),
                ('project_manager', models.CharField(default='Unassigned', max_length=100, verbose_name='项目经理')),
                ('description', models.TextField(blank=True, default='No description provided', verbose_name='描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
    ]
