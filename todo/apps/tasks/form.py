# -*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import Task

class TaskBoardForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name',]
