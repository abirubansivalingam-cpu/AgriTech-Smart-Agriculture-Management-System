from django.db import models
from django.contrib.auth.models import User
class ProduceListing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="produce_listings")
    crop_name = models.CharField(max_length=100)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=9, decimal_places=2)
    location = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.crop_name} by {self.owner.username}"
