from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    return HttpResponse("Home Page")
