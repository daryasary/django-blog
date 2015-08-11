from django.conf.urls import url
import views

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
]