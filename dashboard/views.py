from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def hello(request):
   ## text = """<h1>Welcome to your dashboard!!</h1>"""
   ## return HttpResponse(text)
   template = loader.get_template('welcome.html')
   context = {}
   return HttpResponse(template.render(context, request))