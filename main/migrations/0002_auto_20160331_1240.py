# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(default='\u4ec0\u4e48\u90fd\u6ca1\u6709', max_length=500, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u7528\u6237\u53d1\u5e03\u5185\u5bb9',
                'verbose_name_plural': '\u7528\u6237\u53d1\u5e03\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='Express',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contain_text', models.CharField(max_length=200, verbose_name='\u8868\u767d\u6587\u5b57\u5185\u5bb9', blank=True)),
                ('contain_pic', models.CharField(max_length=200, verbose_name='\u8868\u767d\u56fe\u7247\u5185\u5bb9', blank=True)),
                ('contain_voice', models.CharField(max_length=200, verbose_name='\u8868\u767d\u8bed\u97f3', blank=True)),
                ('like', models.IntegerField(default=0, verbose_name='\u70b9\u8d5e\u4eba\u6570')),
                ('collection', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('share', models.IntegerField(default=0, verbose_name='\u5206\u4eab\u6b21\u6570')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-like'],
                'verbose_name': '\u7528\u6237\u53d1\u5e03\u5185\u5bb9',
                'verbose_name_plural': '\u7528\u6237\u53d1\u5e03\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(verbose_name='\u64cd\u4f5c\u7c7b\u578b', choices=[(0, '\u6d4f\u89c8\u5386\u53f2'), (1, '\u6536\u85cf\u7684'), (2, '\u70b9\u8d5e\u7684'), (3, '\u5206\u4eab\u7684'), (4, '\u56de\u590d\u7684')])),
                ('express', models.ForeignKey(to='main.Express')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u64cd\u4f5c\u8bb0\u5f55',
                'verbose_name_plural': '\u7528\u6237\u64cd\u4f5c\u8bb0\u5f55',
            },
        ),
        migrations.RemoveField(
            model_name='info',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-create_time'], 'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default=2, max_length=200, verbose_name='\u7528\u6237\u5934\u50cf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=120, verbose_name='\u767b\u9646\u90ae\u7bb1', blank=True),
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.AddField(
            model_name='timeline',
            name='user',
            field=models.OneToOneField(to='main.User'),
        ),
        migrations.AddField(
            model_name='express',
            name='user',
            field=models.ForeignKey(to='main.User'),
        ),
        migrations.AddField(
            model_name='comments',
            name='express',
            field=models.ForeignKey(to='main.Express'),
        ),
    ]
