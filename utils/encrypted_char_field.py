from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models

# Fernet.generate_key() 生成密钥保存在配置文件中
cipher_suite = Fernet(settings.KEY)

class EncryptedCharField(models.CharField):
    def get_prep_value(self, value):
        if value is not None:
            value = value.encode('utf-8')
            encrypted_value = cipher_suite.encrypt(value)
            return encrypted_value.decode('utf-8')
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            value = value.encode('utf-8')
            decrypted_value = cipher_suite.decrypt(value)
            return decrypted_value.decode('utf-8')
        return value
