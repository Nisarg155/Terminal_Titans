from django.shortcuts import render
from .models import hospital_details

def home(request):
    hospitals = hospital_details.objects.all()
    return render(request, 'home.html', {'hospitals': hospitals})