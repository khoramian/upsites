from django.shortcuts import render
from django.http import HttpResponse   # delete ///////////////////////////////////////////
from site_management.models import Websites


def list_websites(request):
    websites = Websites.objects.all()
    return HttpResponse("salam")
