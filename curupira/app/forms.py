"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class AddMonitredCityForm(forms.Form):
    pName = forms.CharField(label="Name",
                            max_length=254,
                            widget=forms.TextInput({
                                'class': 'form-control'
                            }))
    pLat = forms.FloatField(label="Latitude",
                            widget = forms.NumberInput({
                                'class': 'form-control',
                            }))
    pLng = forms.FloatField(label="Longitude",
                            widget = forms.NumberInput({
                                'class': 'form-control',
                            }))