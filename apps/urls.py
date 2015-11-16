from django.conf.urls import patterns, include, url
# from django.contrib import admin
from tastypie import api
from restapi_app.resources.markets import MarketResource

v1_api = api.Api(api_name="v1")
v1_api.register(MarketResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(v1_api.urls)),
)
