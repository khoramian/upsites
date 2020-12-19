from django.shortcuts import render
from site_management.models import Websites


def list_websites(request):
    websites = Websites.objects.all()
    retirn render()