from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'garoapush.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^check/', 'main.views.check', name='check'),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^register/', 'main.views.register', name='register'),
)
