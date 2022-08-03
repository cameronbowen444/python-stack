from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is great for our first app!")

def next(request):
    return HttpResponse("thats the next one for our first app!")
