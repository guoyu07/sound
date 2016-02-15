# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=50, verbose_name='\u6635\u79f0')),
                ('mail', models.CharField(max_length=120, verbose_name='\u767b\u9646\u90ae\u7bb1')),
                ('password', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('change_password', models.CharField(default=b'none', max_length=10, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('action_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u7528\u6237\u9a8c\u8bc1\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u9a8c\u8bc1\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='info',
            name='user',
            field=models.ForeignKey(to='main.User'),
        ),
    ]
