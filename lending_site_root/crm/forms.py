from django import forms
from django.forms.widgets import TextInput

class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=TextInput({'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=TextInput({'class': 'form-control'}))