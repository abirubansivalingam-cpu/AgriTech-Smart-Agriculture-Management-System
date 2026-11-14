from django import forms
from .models import Farm, Crop, FarmTask, SoilRecord
class FarmForm(forms.ModelForm):
    class Meta:
        model=Farm; fields=["name","location","area_acres","soil_type","notes"]
class CropForm(forms.ModelForm):
    class Meta:
        model=Crop; fields=["farm","name","season","planted_on","expected_harvest","area_acres","status","notes"]
    def __init__(self,*args,**kwargs):
        user=kwargs.pop("user",None); super().__init__(*args,**kwargs)
        if user: self.fields["farm"].queryset=Farm.objects.filter(owner=user)
class TaskForm(forms.ModelForm):
    class Meta:
        model=FarmTask; fields=["farm","title","due_date","priority"]
    def __init__(self,*args,**kwargs):
        user=kwargs.pop("user",None); super().__init__(*args,**kwargs)
        if user: self.fields["farm"].queryset=Farm.objects.filter(owner=user)
class SoilForm(forms.ModelForm):
    class Meta:
        model=SoilRecord; fields=["farm","recorded_on","ph","nitrogen","phosphorus","potassium","notes"]
    def __init__(self,*args,**kwargs):
        user=kwargs.pop("user",None); super().__init__(*args,**kwargs)
        if user: self.fields["farm"].queryset=Farm.objects.filter(owner=user)
