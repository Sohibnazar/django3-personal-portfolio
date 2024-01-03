from django.shortcuts import render
from .models import Project


def homep(request):
    projects = Project.objects.all()
    return render(request, 'portfoliop/homep.html', {'projects': projects})
