from .models import hospital_details
from .models import Doctor
from .models import User

from django.contrib import admin

# Register your models here.
admin.site.register(hospital_details)
admin.site.register(Doctor)
admin.site.register(User)


from django.contrib import admin
from .models import Doctor,hospital_details,User
# Register your models here.

admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(hospital_details)
