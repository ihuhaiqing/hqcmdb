from django.db import models
from resource.models import Host
from django.contrib.auth.hashers import make_password, check_password

class MySQL(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='实例名称')
    host = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name='主机')
    port = models.IntegerField(default=3306, verbose_name='端口号')
    user = models.CharField(max_length=100, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    database = models.CharField(max_length=100, verbose_name='数据库名称')

    class Meta:
        verbose_name = 'MySQL'
        verbose_name_plural = 'MySQL'

    def save(self, *args, **kwargs):
        # 仅在密码未加密时进行加密
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super(MySQL, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_plain_password(self):
        # 返回明文密码（仅用于显示，不建议在生产环境中使用）
        return self.password
