# -*- coding: UTF-8 -*-
from django.db import models

from .constants import STATUS_CHOICES

class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(default='A', max_length=1, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(null=True, blank=True)

    class Meta():
        ordering = ['order', '-date']
