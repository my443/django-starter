from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to your dashboard!!</h1>"""
   return HttpResponse(text)