# Generated by Django 5.0 on 2024-08-30 07:18

import utils.encrypted_char_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0006_host_environment'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='password',
            field=utils.encrypted_char_field.EncryptedCharField(default='123', max_length=255, verbose_name='密码'),
            preserve_default=False,
        ),
    ]
