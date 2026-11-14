from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Farm,FarmTask
from .forms import FarmForm,CropForm,TaskForm,SoilForm
@login_required
def farm_list(request):
    return render(request,"farms/farm_list.html",{"farms":Farm.objects.filter(owner=request.user)})
@login_required
def farm_create(request):
    form=FarmForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False); obj.owner=request.user; obj.save()
        messages.success(request,"Farm added successfully."); return redirect("farm_list")
    return render(request,"shared/form_page.html",{"form":form,"heading":"Add a farm"})
@login_required
def farm_detail(request,pk):
    farm=get_object_or_404(Farm,pk=pk,owner=request.user)
    return render(request,"farms/farm_detail.html",{"farm":farm})
@login_required
def crop_create(request):
    form=CropForm(request.POST or None,user=request.user)
    if form.is_valid():
        form.save(); messages.success(request,"Crop saved."); return redirect("dashboard")
    return render(request,"shared/form_page.html",{"form":form,"heading":"Add a crop"})
@login_required
def task_create(request):
    form=TaskForm(request.POST or None,user=request.user)
    if form.is_valid():
        form.save(); messages.success(request,"Task created."); return redirect("dashboard")
    return render(request,"shared/form_page.html",{"form":form,"heading":"Create farm task"})
@login_required
def task_toggle(request,pk):
    task=get_object_or_404(FarmTask,pk=pk,farm__owner=request.user)
    if request.method=="POST":
        task.completed=not task.completed; task.save()
    return redirect("dashboard")
@login_required
def soil_create(request):
    form=SoilForm(request.POST or None,user=request.user)
    if form.is_valid():
        form.save(); messages.success(request,"Soil record saved."); return redirect("recommendations")
    return render(request,"shared/form_page.html",{"form":form,"heading":"Add soil test"})
@login_required
def recommendations(request):
    farms=Farm.objects.filter(owner=request.user).prefetch_related("soil_records","crops")
    results=[]
    for farm in farms:
        latest=farm.soil_records.order_by("-recorded_on").first()
        if latest and latest.ph < 5.5: advice="Soil is acidic. Consider a local agricultural officer's advice on liming and retest before application."
        elif latest and latest.ph > 7.5: advice="Soil is alkaline. Check crop suitability and nutrient availability with a soil expert."
        elif latest: advice="Recorded pH is within a commonly suitable range for many crops. Match recommendations to the crop and local conditions."
        else: advice="Add a recent soil test to receive a basic pH-based note."
        results.append({"farm":farm,"soil":latest,"advice":advice})
    return render(request,"farms/recommendations.html",{"results":results})
