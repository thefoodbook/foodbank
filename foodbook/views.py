import requests
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Image

def index(request):
    context = ''
    images = Image.objects.all()
    return render(request, 'foodbook/index.html', {'images': images})

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
    return render(request, 'foodbook/restaurant.html')

def user(request,id):
    return HttpResponse(id)

def events(request, id):
    url = 'http://terminal2.expedia.com/x/activities/search?location=London&apikey=0dPXLNGVjZvLEJXsxLvEoCpbEyJl01Lx'
    response = requests.get(url)
    return render(request, 'foodbook/nearby.html', {'nearby': response.json() })
