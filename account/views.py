from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):
	if request.method == 'POST':
		# return HttpResponse('YOU ARE LOGGED IN')
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponse('Success!!')
			else:
				return HttpResponse('USER IS NOT ACTIVE')
		else:
			return HttpResponse('Wrong username and password %s, %s' %(username, password))

	else:
		return render(request, 'account/login.html')

def register(request):
	return render(request, 'account/register.html')