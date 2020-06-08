from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.views.generic import View
from .utils import ObjectDetailMixin

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def projects_list(request):
    projects = Project.objects.all().order_by('-date_pub')
    return render(request, 'website/projects_list.html', context={'projects': projects})

class ProjectDetail(ObjectDetailMixin, View):
    model = Project
    template = 'website/project_detail.html'