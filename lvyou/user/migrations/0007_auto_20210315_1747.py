# Generated by Django 2.2 on 2021-03-15 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_node_num'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Node',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]