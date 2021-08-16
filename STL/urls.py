from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
# from .view import RunCaseView, RunUiView
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('api/user/', include('stluser.urls')),
    path('api/stl/', include('stlapp.urls')),
]
