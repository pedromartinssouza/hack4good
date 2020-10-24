"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .utils import utils
from .utils import writeDB
from .utils import readDB
from .forms import AddMonitredCityForm

import json
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def monitoring(request):
    """Renders the monitoring page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/monitoring.html',
        {
            'title':'Monitoring',
            'year':datetime.now().year,
            'localizations': readDB.readMonitoring()
        }
    )

def cities(request):
    form = AddMonitredCityForm()
    if request.method == 'GET':
        """Renders the cities page."""
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/cities.html',
            {
                'title':'Cities',
                'year':datetime.now().year,
                'form': form
            }
        )

def saveCity(request):
    form = AddMonitredCityForm()
    if request.method == 'POST':
        writeDB.assignMonitoring(float(request.POST['pLat']), float(request.POST['pLng']), request.POST['pName'])
        return render(
            request,
            'app/cities.html',
            {
                'title':'Cities',
                'year':datetime.now().year,
                'form': form
            }
        )
def getWeather(request, lat, longit, tempUnit):
    if request.method == 'GET':

        return JsonResponse(utils.getWeatherData(lat, longit, tempUnit), safe = False)

def monitorLocation(request, lat, longit, name):
    if request.method == 'POST':
        return JsonResponse(writeDB.assignMonitoring(lat, longit, name), safe = False)

def getLocalizations(request):
    if request.method == 'GET':
        return JsonResponse(readDB.readMonitoring(), safe = False)
