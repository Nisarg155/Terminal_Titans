from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Doctor, User  # Add import statement for the User model

def test (request):
    return HttpResponse("Hello World")
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
