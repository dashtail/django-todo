# -*- coding: UTF-8 -*-
from django.conf.urls import url

from .views import TaskBoardView, reorder_tasks, update_task, delete_task

urlpatterns = [
    url(r'^$', TaskBoardView.as_view()),
    url(r'^reorder/', reorder_tasks),
    url(r'^update/', update_task),
    url(r'^delete/', delete_task),
]
