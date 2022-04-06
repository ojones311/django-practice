from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(req):
    return HttpResponse('Welcome to our page')

def january(req):
    return HttpResponse('Read for 30 minutes a day')
    
def february(req):
    return HttpResponse('Run two miles daily')