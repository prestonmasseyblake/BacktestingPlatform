from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stocks.urls')),
    path('user/',include('user.urls')),
    path('build/',include('build.urls')),
    # path('crypto/',include('crypto.urls')),
    path('documentation/',include('documentation.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
