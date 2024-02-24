from django.shortcuts import render
from .models import Doctor
from .models import hospital_details

def doctor_detail(request):
    doctors=Doctor.objects.all()
    context={
        'doctors':doctors
    }
    return render(request,'doctor_view.html',context)
# Create your views here.


def home(request):
    hospitals = hospital_details.objects.all()
    return render(request, 'home.html', {'hospitals': hospitals})