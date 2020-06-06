from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.views.generic import View

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'website/projects_list.html', context={'projects': projects})

class ProjectCreate(View):
    pass 
