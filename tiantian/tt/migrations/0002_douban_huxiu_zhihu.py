# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-09 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Douban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('author_url', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.CharField(blank=True, max_length=64, null=True)),
                ('book_name', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('book_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'douban',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Huxiu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=128, null=True)),
                ('author_url', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('time', models.CharField(blank=True, max_length=48, null=True)),
            ],
            options={
                'db_table': 'huxiu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zhihu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=48, null=True)),
                ('time', models.CharField(blank=True, max_length=48, null=True)),
                ('author', models.CharField(blank=True, max_length=96, null=True)),
                ('author_url', models.CharField(blank=True, max_length=256, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=48, null=True)),
            ],
            options={
                'db_table': 'zhihu',
                'managed': False,
            },
        ),
    ]