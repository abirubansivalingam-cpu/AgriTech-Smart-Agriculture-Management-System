from django.urls import path
from . import views
urlpatterns=[
 path("",views.farm_list,name="farm_list"), path("new/",views.farm_create,name="farm_create"),
 path("<int:pk>/",views.farm_detail,name="farm_detail"), path("crops/new/",views.crop_create,name="crop_create"),
 path("tasks/new/",views.task_create,name="task_create"), path("tasks/<int:pk>/toggle/",views.task_toggle,name="task_toggle"),
 path("soil/new/",views.soil_create,name="soil_create"), path("recommendations/",views.recommendations,name="recommendations"),
]
