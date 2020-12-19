from django.contrib import admin
from django.urls import path
from site_management.views import list_websites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('site_management/list', list_websites),
]
