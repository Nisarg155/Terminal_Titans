from django.urls import path
from . import views

urlpatterns = [
    path('doctor/',views.doctor_detail,name='doctor_detail')
]
