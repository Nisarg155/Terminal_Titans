from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

app_name = 'hospital'
urlpatterns = [
    path("home/",views.home,name="home"),
    path('doctor/<int:id>',views.doctor_detail,name='doctor_detail'),
    path('Dregister/',views.Dregister,name='Dregister'),
    path('Uregister/', views.Uregister, name='Uregister'),
    path('Appointment/', views.Appointment, name='Appointment'),
    path('<str:specialist>/', views.filter_by_specialist, name='filter_by_specialist'),

]