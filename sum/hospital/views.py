# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response("index.html")
# Create your views here.
