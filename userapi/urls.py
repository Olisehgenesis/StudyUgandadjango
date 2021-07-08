from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from userapi import views

from rest_framework import routers
from userapi.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    #other paths
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
    path('account/register', views.UserCreate.as_view())
]