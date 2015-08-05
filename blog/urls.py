from django.conf.urls import url
from blog import views


urlpatterns = [
	url(r'^category/(?P<cat>.*)$', views.blog_list, name='blog_post_list_cat'),
	url(r'^tag/(?P<tag>.*)$', views.blog_list, name='blog_post_list_tag'),
	url(r'^archive/year/(?P<year>\d{4})/month/(?P<month>\d{1,2})$', views.blog_list, name='blog_post_list_year_month'),
	url(r'^archive/year/(?P<year>\d{4})$', views.blog_list, name='blog_post_list_year'),
	url(r'^post/(?P<slug>.*)/$', views.single_post, name='blog_single'),
	url(r'^$', views.blog_list, name="blog_post_list"),
]