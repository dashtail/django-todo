# -*- coding: UTF-8 -*-
import json
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import render

from .form import *
from .models import *

class TaskBoardView(TemplateView):
    form_class = TaskBoardForm
    template_name = "task/taskboard.html"

    def todo(self):
        tasks = Task.objects.filter(status="A")
        return tasks

    def doing(self):
        tasks = Task.objects.filter(status="E")
        return tasks

    def done(self):
        tasks = Task.objects.filter(status="F")
        return tasks

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_task = form.save()
            return HttpResponse(json.dumps(new_task.pk), content_type="application/json")

        return render(request, self.template_name, {'form': form})

def reorder_tasks(request):
    if request.method == 'POST':
        for i, item in  enumerate(request.POST.getlist('tasks_list[]')):
            task = Task.objects.get(pk=item)
            task.order = i
            task.status = request.POST.get('status')
            task.save()

    return HttpResponse(json.dumps("ok"), content_type="application/json")

def update_task(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        name = request.POST.get('name')
        task = Task.objects.filter(pk=pk).update(name=name)

        return HttpResponse(json.dumps('ok'), content_type="application/json")

def delete_task(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        name = request.POST.get('name')
        task = Task.objects.filter(pk=pk).delete()

        return HttpResponse(json.dumps('ok'), content_type="application/json")
