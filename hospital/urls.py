from django.urls import path
from . import views

app_name = 'hospital'
urlpatterns = [
    path("home",views.home,name="home"),
    path('doctor/',views.doctor_detail,name='doctor_detail')
]