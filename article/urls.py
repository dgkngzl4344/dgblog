from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("create/",views.index),
  path("dashboard/",views.dashboard,name="dashboard"),
path("addarticle/",views.addarticle,name="addarticle"),
path("article/<int:id>/",views.details,name="details"),
path("delete/<int:id>/",views.delete,name="delete"),
path("uptade/<int:id>/",views.uptade,name="uptade"),
path("",views.articles,name="articles"),
path("comment/<int:id>",views.comment,name="comment"),
]

