from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/', include('userapi.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
]