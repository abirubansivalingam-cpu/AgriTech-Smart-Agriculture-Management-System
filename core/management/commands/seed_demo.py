from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from farms.models import Farm,Crop,FarmTask,SoilRecord
from marketplace.models import ProduceListing
from datetime import date,timedelta
class Command(BaseCommand):
    help="Create sample AgriTech demo records"
    def handle(self,*args,**options):
        user,created=User.objects.get_or_create(username="demo_farmer",defaults={"email":"demo@example.com"})
        if created: user.set_password("AgriDemo@123"); user.save()
        farm,_=Farm.objects.get_or_create(owner=user,name="Green Valley Farm",defaults={"location":"Erode, Tamil Nadu","area_acres":3.5,"soil_type":"Red","notes":"Demonstration farm"})
        Crop.objects.get_or_create(farm=farm,name="Turmeric",defaults={"season":"Monsoon","planted_on":date.today()-timedelta(days=30),"expected_harvest":date.today()+timedelta(days=210),"area_acres":2,"status":"growing"})
        FarmTask.objects.get_or_create(farm=farm,title="Inspect irrigation lines",defaults={"due_date":date.today()+timedelta(days=3),"priority":"medium"})
        SoilRecord.objects.get_or_create(farm=farm,recorded_on=date.today(),defaults={"ph":6.5,"nitrogen":45,"phosphorus":22,"potassium":180})
        ProduceListing.objects.get_or_create(owner=user,crop_name="Turmeric",defaults={"quantity_kg":500,"price_per_kg":85,"location":"Erode, Tamil Nadu","description":"Sample listing for demonstration"})
        self.stdout.write(self.style.SUCCESS("Demo data ready. Login: demo_farmer / AgriDemo@123"))
