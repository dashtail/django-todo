# -*- coding: UTF-8 -*-
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('todo.apps.tasks.urls')),
]
