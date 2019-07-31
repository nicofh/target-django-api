from django.urls import include, path
from rest_framework import routers
from api import views
from .views import FacebookLogin

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
