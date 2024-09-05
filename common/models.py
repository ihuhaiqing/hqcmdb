from django.db import models
from django.contrib.auth.models import User

class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称', default='Red Hat Enterprise Linux')
    version = models.CharField(max_length=50, verbose_name='版本', default='9.0')

    class Meta:
        verbose_name = '操作系统'
        verbose_name_plural = '操作系统'

    def __str__(self):
        return f"{self.name} {self.version}"


class Environment(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='环境名称', default='stage')
    description = models.TextField(blank=True, verbose_name='描述', default='No description provided')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '开发环境'
        verbose_name_plural = '开发环境'

    def __str__(self):
        return self.name
    

class Project(models.Model):
    STATUS_CHOICES = [
        ('online', '在线'),
        ('offline', '下线'),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name='项目名称', default='New Project')
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, verbose_name='状态', default='online')
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='项目经理', related_name='project_manager')
    users = models.ManyToManyField(User, verbose_name='用户')
    description = models.TextField(blank=True, verbose_name='描述', default='No description provided')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name
