from django.shortcuts import render, HttpResponse

def next(request):
    return HttpResponse("Hello Next Route!")

def second(request):
    return HttpResponse("Thats right")

# Create your views here.
