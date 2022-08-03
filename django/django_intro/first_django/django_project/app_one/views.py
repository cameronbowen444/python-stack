from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return redirect("blogs/")

def blogs(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
# Create your views here.

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("placeholder to display blog number: {number}")