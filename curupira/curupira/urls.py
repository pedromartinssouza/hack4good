"""
Definition of urls for curupira.
"""

from datetime import datetime
from django.urls import register_converter, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from . import converters

register_converter(converters.NegativeIntConverter, 'negint')


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('getWeather/<negint:lat>/<negint:longit>', views.getWeather),
    path('monitorLocation/<negint:lat>/<negint:longit>', views.monitorLocation)
]
