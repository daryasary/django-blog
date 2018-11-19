from __future__ import unicode_literals

from django.conf.urls import url
from blog.admin import blog_admin_site
from blog.views import blog_list, single_post
from settings import BLOG_SETTINGS

urlpatterns = [
    url(r'^category/(?P<cat>.*)$', blog_list, name='blog_post_list_cat'),
    url(r'^tag/(?P<tag>.*)$', blog_list, name='blog_post_list_tag'),
    url(r'^archive/year/(?P<year>\d{4})/month/(?P<month>\d{1,2})$', blog_list, name='blog_post_list_year_month'),
    url(r'^archive/year/(?P<year>\d{4})$', blog_list, name='blog_post_list_year'),
    url(r'^post/(?P<slug>.*)/$', single_post, name='blog_single'),
    url(r'^$', blog_list, name="blog_post_list"),
]

if BLOG_SETTINGS['ENABLE_CUSTOM_PANEL']:
    urlpatterns += [url(r'{}'.format(BLOG_SETTINGS['ADMIN_PANEL_URL']), blog_admin_site.urls, name='blog_admin')]