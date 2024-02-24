from django.db import models


class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=40)
    specialist=models.CharField(max_length=30)
    experience_in_year=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='doctor/')


    def __str__(self):
        return self.name
    

# Create your models here.
class hospital_details(models.Model):
    hospital_img = models.ImageField(upload_to="hospital/")
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name
    

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    blood_group = models.CharField(max_length=5)
    mobile_no = models.IntegerField(max_length=10)
    allergies_description = models.TextField(blank=True,null=True)


