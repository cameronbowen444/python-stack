from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Response from our index!")

def one(request):
    return HttpResponse("This is a cool feature!")

def one_method(request):
    pass

def another_method(request, my_val):
    pass

def yet_another(request, name):
    pass

def one_more(request, id, color):
    pass