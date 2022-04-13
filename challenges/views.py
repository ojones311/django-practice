from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from .month import challenges
# Create your views here.

#Create a month dict that maps a month to an activity
#Pass the month dynamically which I say we would get it from the url

def index(req):
    list_items= ""
    months= list(challenges.keys())
    list_items = [f'<ul><h3>{x}</h3></ul>' for x in months]
    return HttpResponse(list_items)

def monthly_challenge_by_number(req, month):
    months = list(challenges.keys())
    if(month > len(months)):
        return HttpResponseNotFound('Month out of rang')
    redirect_month = months[month -1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        month = month[0].upper() + month[1:len(month)]
        challenge_text = challenges[month]
        response_data = f"<h4>In {month} my goal is to  {challenge_text}</h4>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h4>Please use a valid month</h4>')