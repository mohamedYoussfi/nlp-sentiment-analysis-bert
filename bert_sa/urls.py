from django.contrib import admin
from django.urls import path
from bert_sa import api

urlpatterns = [path("admin/", admin.site.urls), path("test/", api.test)]
