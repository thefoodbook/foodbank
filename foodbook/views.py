from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question

def index(request):
	context = ''
	return render(request, 'foodbook/index.html')


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
    return HttpResponse(id)

def user(request,id):
    return HttpResponse(id)


#def restaurant(request,id):
#    return HttpResponse("")
#    