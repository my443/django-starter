from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required         ## For Authentication
from django.views.generic.edit import UpdateView                  ## For Updating the view

from .models import ProjectData

@login_required(login_url='/person/login/')
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

   return render(request, 'welcome.html', context)       ## This seems to be an easier way to return a template.
                                                         ## https://docs.djangoproject.com/en/4.1/intro/tutorial03/

   #return HttpResponse(template.render(context, request))

##@login_required(login_url='/person/login/')
class Update(UpdateView):
   model = ProjectData                             # model
   fields = '__all__'                              # fields / if you want to select all fields, use "__all__"
   fields = ['project_name', 'description', 'record_date']     # but if you are doing specific fields, you have to name them.
   template_name = 'update_project.html'              # template for updating
   success_url = "/dashboard"                          # posts list url

   def post(self, request, *args, **kwargs):
      ##self.referer = request.session.get("login_referer", "")
      return super().post(request, *args, **kwargs)