# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0024_auto_20160817_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item002',
            name='id',
        ),
        migrations.AlterField(
            model_name='item002',
            name='field1',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='編號'),
        ),
        migrations.AlterField(
            model_name='item002',
            name='field2',
            field=models.CharField(default='.', max_length=200, verbose_name='客戶'),
        ),
        migrations.AlterField(
            model_name='item002',
            name='field3',
            field=models.CharField(default='.', max_length=200, verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='item002',
            name='field4',
            field=models.CharField(default='.', max_length=200, verbose_name='欠料量'),
        ),
        migrations.AlterField(
            model_name='item002',
            name='field5',
            field=models.CharField(default='.', max_length=200, verbose_name='欠備庫量'),
        ),
        migrations.AlterField(
            model_name='item002',
            name='field6',
            field=models.CharField(default='.', max_length=200, verbose_name='客訴量'),
        ),
        migrations.AlterField(
            model_name='item002',
            name='field7',
            field=models.CharField(default='.', max_length=200, verbose_name='模具壽命'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field6',
            field=models.CharField(default='.', max_length=200, verbose_name='客訴量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='field7',
            field=models.CharField(default='.', max_length=200, verbose_name='模具壽命'),
        ),
    ]