from django.db import models

class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称', default='Red Hat Enterprise Linux')
    version = models.CharField(max_length=50, verbose_name='版本', default='9.0')

    class Meta:
        verbose_name = '操作系统'
        verbose_name_plural = '操作系统'

    def __str__(self):
        return f"{self.name} {self.version}"
