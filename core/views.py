from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.contrib import messages
from django.utils import timezone
from .forms import RegisterForm
from farms.models import Farm, Crop, FarmTask, SoilRecord
from marketplace.models import ProduceListing
def home(request):
    return render(request,"core/home.html")
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(); login(request,user); messages.success(request,"Your farmer account is ready.")
            return redirect("dashboard")
    else: form=RegisterForm()
    return render(request,"registration/register.html",{"form":form})
@login_required
def dashboard(request):
    farms=Farm.objects.filter(owner=request.user)
    crops=Crop.objects.filter(farm__owner=request.user)
    tasks=FarmTask.objects.filter(farm__owner=request.user,completed=False).order_by("due_date")[:6]
    listings=ProduceListing.objects.filter(owner=request.user,available=True)
    context={"farm_count":farms.count(),"crop_count":crops.count(),
        "growing_count":crops.filter(status="growing").count(),"open_tasks":FarmTask.objects.filter(farm__owner=request.user,completed=False).count(),
        "tasks":tasks,"listings":listings[:4],"farms":farms[:5]}
    return render(request,"core/dashboard.html",context)
