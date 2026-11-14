from django.contrib import admin
from .models import Farm,Crop,FarmTask,SoilRecord
admin.site.register([Farm,Crop,FarmTask,SoilRecord])
