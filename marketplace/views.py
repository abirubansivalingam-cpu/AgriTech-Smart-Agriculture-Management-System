from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ProduceListing
from .forms import ListingForm
@login_required
def listings(request):
    qs=ProduceListing.objects.filter(available=True).select_related("owner").order_by("-created_at")
    q=request.GET.get("q","").strip()
    if q: qs=qs.filter(crop_name__icontains=q)
    return render(request,"marketplace/listings.html",{"listings":qs,"q":q})
@login_required
def create_listing(request):
    form=ListingForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False); obj.owner=request.user; obj.save()
        messages.success(request,"Produce listing published."); return redirect("listings")
    return render(request,"shared/form_page.html",{"form":form,"heading":"List your produce"})
