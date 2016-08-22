# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0030_auto_20160822_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item004xx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f01', models.CharField(default='.', max_length=99, verbose_name='客戶')),
                ('f02', models.CharField(default='.', max_length=99, verbose_name='量產訂單號')),
                ('f03', models.CharField(default='.', max_length=99, verbose_name='產品代碼')),
                ('f04', models.CharField(default='.', max_length=99, verbose_name='產品名稱')),
                ('f05', models.CharField(default='.', max_length=99, verbose_name='計劃交期')),
                ('f06', models.CharField(default='.', max_length=99, verbose_name='訂單量')),
                ('f07', models.CharField(default='.', max_length=99, verbose_name='已交量')),
                ('f08', models.CharField(default='.', max_length=99, verbose_name='未交量')),
                ('f09', models.CharField(default='.', max_length=99, verbose_name='備庫量')),
                ('f10', models.CharField(default='.', max_length=99, verbose_name='欠備庫量')),
                ('f11', models.CharField(default='.', max_length=99, verbose_name='客訴量')),
                ('f12', models.CharField(default='.', max_length=99, verbose_name='模具壽命')),
            ],
        ),
        migrations.DeleteModel(
            name='Item004',
        ),
    ]