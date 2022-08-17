from dataclasses import field
from django import forms

from .models import Meter, Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = (
            "amount",
        )