from django.shortcuts import render
from .models import Doctor
from .models import hospital_details
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Doctor, User  # Add import statement for the User model

def doctor_detail(request,id):
    hospital = hospital_details.objects.get(id=id)
    doctors=Doctor.objects.filter(hospital_detail=hospital)
    context={
        'doctors':doctors
    }
    return render(request,'doctor_view.html',context)
# Create your views here.



def Dregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        specialist = request.POST.get('specialist')
        experience_in_year = request.POST.get('experience_in_year')
        description = request.POST.get('description')
        image = request.POST.get('image')
        license = request.POST.get('license')

        saverecord = Doctor(name=name, email=email, specialist=specialist, experience_in_year=experience_in_year, description=description,
                            image=image, license=license)
        saverecord.save()

    return render(request, 'Dregister.html')

def Uregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood_group = request.POST.get('blood_group')
        mobile_no = request.POST.get('mobile_no')
        allergies_description = request.POST.get('allergies_description')

        saverecord = User(name=name, blood_group=blood_group, mobile_no=mobile_no, allergies_description=allergies_description)
        saverecord.save()

    return render(request, 'Uregister.html')


def home(request):
    hospitals = hospital_details.objects.all()
    return render(request, 'home.html', {'hospitals': hospitals})