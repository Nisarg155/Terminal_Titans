from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('Dregister/',views.Dregister,name='Dregister'),
    path('Uregister/', views.Uregister, name='Uregister'),

]