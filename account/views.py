from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
	# return HttpResponse('Here is login page')
	return render(request, 'account/login.html')

def register(request):
	return render(request, 'account/register.html')