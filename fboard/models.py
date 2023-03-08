from datetime import datetime, timezone
from django.db import models


class Fboard(models.Model):
    f_No = models.AutoField(primary_key=True)
    f_Title = models.CharField(max_length=100)
    f_Detail = models.CharField(max_length=3000)
    f_writer = models.CharField(max_length=100)
    f_group = models.IntegerField(default=0)
    f_step = models.IntegerField(default=0)
    f_indent = models.IntegerField(default=0)
    f_createdate = models.DateTimeField(default=datetime.now(), blank=True)
    f_updatedate = models.DateTimeField(default=datetime.now(), blank=True)
    f_hit = models.IntegerField(default=1)

    def __str__(self):
        return self.f_Title


class Lboard(models.Model):
    L_No = models.AutoField(primary_key=True)
    L_writer = models.CharField(max_length=100)
    L_Title = models.CharField(max_length=100)
    L_Detail = models.CharField(max_length=1000)
    L_createdate = models.DateTimeField(default=datetime.now(), blank=True)
    L_updatedate = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.L_Title
