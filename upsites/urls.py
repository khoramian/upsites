from django.contrib import admin
from django.urls import path
from site_management.models import Websites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('site_management/list', ),
]
