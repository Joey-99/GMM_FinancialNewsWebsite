# Generated by Django 2.2 on 2021-03-15 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210315_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('content', models.TextField(verbose_name='公告')),
                ('date', models.DateField(auto_now_add=True, verbose_name='公告时间')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='地名')),
                ('content', models.TextField(verbose_name='旅游介绍')),
                ('pic', models.ImageField(upload_to='media', verbose_name='经典图片')),
                ('num', models.IntegerField(default=0, verbose_name='浏览量')),
                ('collect_num', models.IntegerField(default=0, verbose_name='收藏量')),
                ('lat', models.FloatField(null=True, verbose_name='纬度')),
                ('long', models.FloatField(blank=True, verbose_name='经度')),
                ('user', models.ManyToManyField(blank=True, null=True, to='user.User', verbose_name='景点收藏者')),
            ],
            options={
                'verbose_name': '景点',
                'verbose_name_plural': '景点',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='留言内容')),
                ('date', models.DateField(auto_now_add=True, verbose_name='留言时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '留言板',
                'verbose_name_plural': '留言板',
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='路线名称')),
                ('content', models.TextField(verbose_name='路线介绍')),
                ('station', models.ManyToManyField(to='user.Station', verbose_name='旅游路线')),
                ('user', models.ManyToManyField(blank=True, null=True, to='user.User', verbose_name='景点收藏者')),
            ],
            options={
                'verbose_name': '旅游路线',
                'verbose_name_plural': '旅游路线',
            },
        ),
    ]