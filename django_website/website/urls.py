from django.urls import path
from .views import index, projects_list, ProjectDetail
from django.urls import re_path

urlpatterns = [
    path('', index),
    re_path(r'^projects', projects_list, name="projects_list_url"),
    path('project/<str:slug>', ProjectDetail.as_view(), name="project_detail_url"),
]