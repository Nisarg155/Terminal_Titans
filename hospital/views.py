from datetime import date, time

from django.shortcuts import render
from .models import Doctor
from .models import hospital_details
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Doctor, User  # Add import statement for the User model


def doctor_detail(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'doctor_view.html', context)


# Create your views here.


def Dregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile= request.POST.get('mobile')
        specialist = request.POST.get('specialist')
        experience_in_year = request.POST.get('experience_in_year')
        description = request.POST.get('description')
        image = request.POST.get('image')
        license = request.POST.get('license')
        D_id = request.COOKIES.get('uid')

        saverecord = Doctor(D_id=D_id, name=name, mobile=mobile,specialist=specialist,
                            experience_in_year=experience_in_year, description=description,
                            image=image, license=license)
        saverecord.save()
        redirect('hospital:home')

    return render(request, 'Dregister.html')


def Uregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood_group = request.POST.get('blood_group')
        mobile_no = request.POST.get('mobile_no')
        allergies_description = request.POST.get('allergies_description')
        uid = request.COOKIES.get('uid')
        saverecord = User(user_id=uid, name=name, blood_group=blood_group, mobile_no=mobile_no,
                          allergies_description=allergies_description)
        saverecord.save()
        redirect('hospital:home')

    return render(request, 'Uregister.html')

def Appointment(request):

            if request.method == 'POST':
                user = User.objects.get(id=request.POST['user_id'])
                doctor = Doctor.objects.get(id=request.POST['doctor_id'])
                appointment_date = date.fromisoformat(request.POST['date'])
                appointment_time = time.fromisoformat(request.POST['time'])
                # Add other fields as needed

                appointment = Appointment.objects.create(user=user, doctor=doctor, date=appointment_date,
                                                         time=appointment_time)
                # Redirect or do additional processing as needed
                return redirect('appointment_success')  # You can create a success page

            # Render the form
            return render(request, 'appointment.html',
                          {'users': User.objects.all(), 'doctors': Doctor.objects.all()})
def home(request):
    hospitals = hospital_details.objects.all()
    return render(request, 'home.html', {'hospitals': hospitals})
