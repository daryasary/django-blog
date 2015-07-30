from django.conf.urls import include, url
from django.contrib import admin
from . import views as home

urlpatterns = [
    # Examples:
    # url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home.index, name = 'home'),
    url(r'^blog/', include('blog.urls'), name='blog'),
]
