from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/', include('userapi.urls')),
    path(r'', include('django.contrib.auth.urls')),
]