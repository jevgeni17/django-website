from django.urls import path
from .views import index, projects_list, ProjectCreate
from django.urls import re_path

urlpatterns = [
    path('', index),
    re_path(r'^projects', projects_list, name="projects_list_url"),
    re_path(r'^projects/create-new', ProjectCreate.as_view(), name="project_create_url"),
]