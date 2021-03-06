# Generated by Django 2.2 on 2021-01-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200502_0436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '普通用户'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='isLogin',
            field=models.BooleanField(default=False, verbose_name='登录状态'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, unique=True, verbose_name='账号'),
        ),
    ]
