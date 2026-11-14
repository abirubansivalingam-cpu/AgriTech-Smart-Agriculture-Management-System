from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from farms.models import Farm,Crop
class AgriTechTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="farmer1",password="TestPass123!")
    def test_home_page(self):
        self.assertEqual(self.client.get(reverse("home")).status_code,200)
    def test_register_page(self):
        self.assertEqual(self.client.get(reverse("register")).status_code,200)
    def test_dashboard_requires_login(self):
        response=self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code,302)
    def test_dashboard_for_logged_in_farmer(self):
        self.client.login(username="farmer1",password="TestPass123!")
        self.assertEqual(self.client.get(reverse("dashboard")).status_code,200)
    def test_farmer_can_create_farm(self):
        self.client.login(username="farmer1",password="TestPass123!")
        response=self.client.post(reverse("farm_create"),{"name":"Green Field","location":"Erode","area_acres":"2.5","soil_type":"Red","notes":""})
        self.assertEqual(response.status_code,302)
        self.assertTrue(Farm.objects.filter(owner=self.user,name="Green Field").exists())
    def test_user_cannot_view_another_users_farm(self):
        other=User.objects.create_user(username="other",password="TestPass123!")
        farm=Farm.objects.create(owner=other,name="Private Farm",location="Town",area_acres=1,soil_type="Loamy")
        self.client.login(username="farmer1",password="TestPass123!")
        self.assertEqual(self.client.get(reverse("farm_detail",args=[farm.pk])).status_code,404)
