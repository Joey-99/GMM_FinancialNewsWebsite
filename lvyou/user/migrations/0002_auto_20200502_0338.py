# Generated by Django 2.2.3 on 2020-05-01 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '修改申请', 'verbose_name_plural': '修改申请'},
        ),
        migrations.AddField(
            model_name='house',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户'),
        ),
    ]