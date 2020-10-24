"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .utils import utils

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

<<<<<<< HEAD
def monitoring(request):
    """Renders the monitoring page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/monitoring.html',
        {
            'title':'Monitoring',
            'year':datetime.now().year,
        }
    )
=======
def getWeather(request, lat, longit):
    if request.method == 'GET':
        return utils.getWeatherData(lat, longit)
>>>>>>> 834b923d628ef8dca238fd1ea24ab0160b3337ed
