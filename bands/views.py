from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils import timezone

from .models import band, sponsor


# Create your views here.

def index(request):
    bands = band.objects.all().order_by('priority')
    sponsors = sponsor.objects.all()
    return render(request, 'index.html', {'bands': bands, 'sponsors': sponsors})

def our_story(request):
    return render(request, 'our_story.html')

def band_details(request, pk):
    bandx = get_object_or_404(band, pk=pk)
    return render(request, 'band_detail.html', {'band': bandx})

def sponsor_details(request, pk):
    sponsorx = get_object_or_404(sponsor, pk=pk)
    return render(request, 'sponsor_detail.html', {'sponsor': sponsorx})

def bands(request):
    bands = band.objects.all().order_by('priority')
    return render(request, 'bands.html', {'bands': bands})


def sponsors(request):
    sponsors = sponsor.objects.all()
    return render(request, 'sponsors.html', {'sponsors': sponsors})
