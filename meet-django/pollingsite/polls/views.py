from django.shortcuts import render
from django.http import HttpResponse

from models import Polls, answer
def vote(request):
	return render(request, 'history.html')
# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request
