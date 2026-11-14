from django.db import models
from django.contrib.auth.models import User
class Farm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farms")
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=180)
    area_acres = models.DecimalField(max_digits=8, decimal_places=2)
    soil_type = models.CharField(max_length=80, choices=[("Loamy","Loamy"),("Clay","Clay"),("Sandy","Sandy"),("Black","Black soil"),("Red","Red soil"),("Other","Other")], default="Loamy")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class Crop(models.Model):
    STATUS = [("planned","Planned"),("growing","Growing"),("harvested","Harvested")]
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="crops")
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=60, blank=True)
    planted_on = models.DateField(null=True, blank=True)
    expected_harvest = models.DateField(null=True, blank=True)
    area_acres = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="planned")
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.name} - {self.farm.name}"
class FarmTask(models.Model):
    PRIORITY = [("low","Low"),("medium","Medium"),("high","High")]
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=150)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY, default="medium")
    completed = models.BooleanField(default=False)
    def __str__(self): return self.title
class SoilRecord(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="soil_records")
    recorded_on = models.DateField()
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    nitrogen = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    phosphorus = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    potassium = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    def __str__(self): return f"Soil {self.farm.name} {self.recorded_on}"
