from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is great!")

def next(request):
    return HttpResponse("thats the next one!")
