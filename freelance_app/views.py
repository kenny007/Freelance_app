from django.shortcuts import render
from .models import JobListing

# Create your views here.
def home(request):

    job_listings = JobListing.objects.all();

    return render(request, "freelance_app/index.html", {'job_listings':job_listings})
