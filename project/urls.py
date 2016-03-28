from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'(\d*)\+(\d*)', 'calc.views.sumador'),
    url(r'(\d*)-(\d*)', 'calc.views.restador'),
    url(r'(\d*)\*(\d*)', 'calc.views.multiplicador'),
    url(r'(\d*)/(\d*)', 'calc.views.divisor'),
    url(r'.*', 'calc.views.error')
)
