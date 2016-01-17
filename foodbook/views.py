import requests
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question

def index(request):
	context = ''
	return render(request, 'foodbook/index.html')

def index_temp(request):
	context = ''
	return render(request, 'foodbook/index_1.html')


#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
#
#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
#
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

def restaurant(request,id):
    url = 'http://terminal2.expedia.com/x/hotels?maxhotels=10&location=47.6063889%2C-122.3308333&radius=5km&apikey=0dPXLNGVjZvLEJXsxLvEoCpbEyJl01Lx'
    url = 'http://terminal2.expedia.com/x/geo/features/319476404477494689/features?within=5km&type=hotel&apikey=0dPXLNGVjZvLEJXsxLvEoCpbEyJl01Lx'
    # url = 'http://terminal2.expedia.com/x/geo/features?within=5km&lng=-122.453269&lat=37.777363&type=point_of_interest&apikey=0dPXLNGVjZvLEJXsxLvEoCpbEyJl01Lx'
    response = requests.get(url)
    context = ''
    return render(request, 'foodbook/restaurant.html', {'nearby': response})

def user(request,id):
    return HttpResponse(id)

def events(request, id):
    url = 'http://terminal2.expedia.com/x/activities/search?location=London&apikey=0dPXLNGVjZvLEJXsxLvEoCpbEyJl01Lx'
    response = requests.get(url)
    return render(request, 'foodbook/nearby.html', {'nearby': response.json() })

#def restaurant(request,id):
#    return HttpResponse("")
#    
