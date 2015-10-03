from django.conf.urls import patterns, include, url
from user_api.resources import UserResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(UserResource())

urlpatterns = patterns('',
    # API urls
    (r'^api/', include(v1_api.urls)),
)
