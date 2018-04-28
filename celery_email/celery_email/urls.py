from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from demo_app import viewss

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celery_email.views.home', name='home'),
    # url(r'^celery_email/', include('celery_email.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^index/', viewss.index, name="index")
)
