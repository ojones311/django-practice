from django.shortcuts import render
from django.http import HttpResponse
from .month import activity
# Create your views here.

#Create a month dict that maps a month to an activity
#Pass the month dynamically which I say we would get it from the url

def index(req):
    return HttpResponse('Welcome to our page')

def monthly_challenge(req, month):

    return HttpResponse(f"In {month} my goal is to {activity[month]}")