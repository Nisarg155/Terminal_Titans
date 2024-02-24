from django.db import models
def user_directory_path(instance, filename):
    # Upload the file to a directory based on the model name and instance ID
    return f'{instance.__class__.__name__}/{instance.id}/{filename}'
# Create your models here.
class hospital_details(models.Model):
    hospital_img = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=40)
    specialist=models.CharField(max_length=30)
    experience_in_year=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='doctor/')
    hospital_detail=models.ForeignKey(hospital_details,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to=user_directory_path)


    def __str__(self):
        return self.name
    

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    blood_group = models.CharField(max_length=5)
    mobile_no = models.IntegerField()
    allergies_description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name



