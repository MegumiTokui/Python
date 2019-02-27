from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hi hghgfhfh")

def first(request):
    return render(request, 'newww/home.html')

def about(request):
    return  render(request, 'newww/about.html')

def contact(request):
    return  render(request, 'newww/contact.html')   