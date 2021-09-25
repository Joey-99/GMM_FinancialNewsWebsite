# Generated by Django 2.2 on 2021-03-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20210316_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='company',
            name='file',
            field=models.ImageField(default='aaa', upload_to='media', verbose_name='企业资格证书'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medical',
            name='file',
            field=models.ImageField(default='aa', upload_to='media', verbose_name='企业资格证书'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='x',
            field=models.FloatField(blank=True, null=True, verbose_name='平面X坐标'),
        ),
        migrations.AlterField(
            model_name='company',
            name='y',
            field=models.FloatField(blank=True, null=True, verbose_name='平面Y坐标'),
        ),
    ]
