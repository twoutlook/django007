# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0032_auto_20160822_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item004',
            name='f06',
            field=models.IntegerField(blank=True, null=True, verbose_name='訂單量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='f07',
            field=models.IntegerField(blank=True, null=True, verbose_name='已交量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='f08',
            field=models.IntegerField(blank=True, null=True, verbose_name='未交量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='f09',
            field=models.IntegerField(blank=True, null=True, verbose_name='備庫量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='f10',
            field=models.IntegerField(blank=True, null=True, verbose_name='欠備庫量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='f11',
            field=models.IntegerField(blank=True, null=True, verbose_name='客訴量'),
        ),
        migrations.AlterField(
            model_name='item004',
            name='f12',
            field=models.IntegerField(blank=True, null=True, verbose_name='模具壽命'),
        ),
    ]