# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Douban(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    author_url = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=64, blank=True, null=True)
    book_name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    book_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban'


class Guoke(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author_url = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guoke'


class Huxiu(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=128, blank=True, null=True)
    author_url = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    time = models.CharField(max_length=48, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huxiu'
