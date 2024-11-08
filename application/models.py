from django.db import models
from common.models import Environment, Project
from resource.models import Host
from utils.encrypted_char_field import EncryptedCharField

class MySQL(models.Model):
    database_name = models.CharField(max_length=255, verbose_name="数据库名称", default="database_name")
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, verbose_name="环境")
    host = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name="主机")
    port = models.IntegerField(default=3306, verbose_name="端口号")
    role = models.CharField(max_length=50, verbose_name="角色", choices=[('PRIMARY', 'PRIMARY'), ('SECONDARY', 'SECONDARY')], default='PRIMARY')
    username = models.CharField(max_length=255, verbose_name="用户名", default="root")
    password = EncryptedCharField(max_length=255, verbose_name="密码", default="password")
    version = models.CharField(max_length=50, verbose_name="版本号", default="8.0")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="项目")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
   
    class Meta:
        verbose_name = "MySQL"
        verbose_name_plural = "MySQL"

    def save(self, *args, **kwargs):
        self.environment = self.host.environment
        super(MySQL, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.database_name} on {self.host.hostname}"
