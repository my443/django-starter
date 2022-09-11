from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import ProjectData

def hello(request):
   ## text = """<h1>Welcome to your dashboard!!</h1>"""
   ## return HttpResponse(text)
   project_data = ProjectData.objects.all().values()              ## This is a queryset
   ## project_data = ProjectData.objects.all().values()  ## https://www.w3schools.com/django/django_queryset_get.php

   template = loader.get_template('welcome.html')
   context = {
      'project_data': project_data
   }
   ## context = {}
   return HttpResponse(template.render(context, request))