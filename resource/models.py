from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=100, unique=True, verbose_name='主机名')
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, verbose_name='IP地址')
    operating_system = models.CharField(max_length=100, verbose_name='操作系统')
    cpu_cores = models.IntegerField(verbose_name='CPU核心数')
    memory_gb = models.FloatField(verbose_name='内存(GB)')
    storage_gb = models.FloatField(verbose_name='存储(GB)')
    description = models.TextField(blank=True, verbose_name='描述')  # 新增的描述字段
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '主机'
        verbose_name_plural = '主机'

    def __str__(self):
        return self.hostname
