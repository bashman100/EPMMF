from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils import timezone

from .models import band


# Create your views here.

def index(request):
    bands = band.objects.all()
    return render(request, 'index.html', {'bands': bands})
    sponsors = sponsor.objects.all()
    return render(request, 'index.html', {'sponsors': sponsors})

def band_details(request, pk):
    band = get_object_or_404(band, pk=pk)
    return render(request, 'band_detail.html', {'band': band})

def sponsor_details(request, pk):
    sponsor = get_object_or_404(sponsor, pk=pk)
    return render(request, 'sponsor_detail.html', {'sponsor': sponsor})