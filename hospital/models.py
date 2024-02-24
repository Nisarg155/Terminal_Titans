from django.db import models


class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=40)
    specialist=models.CharField(max_length=30)
    experience_in_year=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='doctor/')
    

# Create your models here.
