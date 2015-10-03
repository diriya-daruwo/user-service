from tastypie.resources import ModelResource
from user_api.models import User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        include_resource_uri = False
        allowed_methods = ['get', 'post', 'put']
        excludes = ['auth_id']
