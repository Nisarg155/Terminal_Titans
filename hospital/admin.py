from django.contrib import admin
from .models import Doctor,hospital_details,User
# Register your models here.

admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(hospital_details)
