from django import forms
from .models import ProduceListing
class ListingForm(forms.ModelForm):
    class Meta:
        model=ProduceListing
        fields=["crop_name","quantity_kg","price_per_kg","location","description","available"]
