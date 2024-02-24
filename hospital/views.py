from django.shortcuts import render
from .models import Doctor

def doctor_detail(request):
    doctors=Doctor.objects.all()
    context={
        'doctors':doctors
    }
    return render(request,'doctor_view.html',context)
# Create your views here.
