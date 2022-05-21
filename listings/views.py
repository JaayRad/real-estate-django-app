from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Listing
from .forms import ListingForm

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)

def listing_create(request):
    if request.method =="POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    form = ListingForm()
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def listing_update(request, pk):


    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method =="POST":
        form = ListingForm(request.POST, instance=listing,files = request.FILES )
        if form.is_valid():
            form.save()
            return redirect('/')
        
    form = ListingForm()
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")


