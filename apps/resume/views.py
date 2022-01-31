from django.shortcuts import render
from apps.resume.models import Project


# Create your views here.


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'resume/index.html', context)
