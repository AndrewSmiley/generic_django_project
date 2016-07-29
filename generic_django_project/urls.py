from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'generic_django_project.views.index', name='index'),
    url(r'^myindex/', 'generic_django_project.views.myindex', name="myindex"),
     # url(r'^blog/', include('blog.urls')),
    url(r'^v1/get_cars/', 'generic_django_project.views.get_cars', name="get_cars"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
