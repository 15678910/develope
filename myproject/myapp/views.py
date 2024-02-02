from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def detail(request):
    return HttpResponse("You're looking at question %s.")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return



