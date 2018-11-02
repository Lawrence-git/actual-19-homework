# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='主机名')),
                ('cpu_num', models.IntegerField(verbose_name='cpu核数')),
                ('cpu_model', models.CharField(max_length=20, verbose_name='cpu型号')),
                ('remark', models.TextField(default='', null=True, verbose_name='备注')),
                ('mem_total', models.CharField(default='8G', max_length=3, verbose_name='内存')),
                ('disk', models.CharField(max_length=4, verbose_name='磁盘大小')),
                ('public_ip', models.CharField(default='', max_length=32, verbose_name='公网ip')),
                ('private_ip', models.CharField(max_length=32, verbose_name='私有ip')),
                ('remote_ip', models.CharField(default='', max_length=32, verbose_name='远程ip')),
                ('op', models.CharField(default='', max_length=32, verbose_name='运维负责人')),
                ('status', models.IntegerField(choices=[(0, '下线'), (1, '在线')], verbose_name='机器的状态0 | 1')),
                ('os_system', models.CharField(max_length=32, verbose_name='操作系统')),
                ('service_line', models.CharField(max_length=32, verbose_name='所属业务线')),
                ('frame', models.CharField(max_length=32, verbose_name='机架')),
                ('use_date', models.DateTimeField(auto_now_add=True, verbose_name='使用日期')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'db_table': 'assets',
            },
        ),
    ]
