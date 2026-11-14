from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FarmerProfile
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    village = forms.CharField(max_length=100, required=False)
    district = forms.CharField(max_length=100, required=False)
    class Meta:
        model = User
        fields = ("username","email","phone","village","district","password1","password2")
    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            FarmerProfile.objects.create(user=user, phone=self.cleaned_data.get("phone",""),
                village=self.cleaned_data.get("village",""), district=self.cleaned_data.get("district",""))
        return user
