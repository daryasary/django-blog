from django.shortcuts import render

# simple view for index page that maps to blog engine
def index(request):
	return render(request,'index.html')