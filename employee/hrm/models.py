from django.db import models

# Create your models here.

class Users(models.Model):
    eid = models.CharField(max_length=10, unique=True) # HQ001
    name = models.CharField(max_length=100) # Nitin Mishra
    email = models.EmailField(max_length=30) # nitin@gmail.com
    mobile = models.CharField(max_length=30)  #999999999
    dob = models.DateField() # 2002-17-01
    gender = models.CharField(max_length=20) # Male
    country = models.CharField(max_length=20) #India
    state = models.CharField(max_length=40) # madhya pradesh
    city =  models.CharField(max_length=40) # Indore

    def upload_photo(self, filename):
        path = 'hrm/photo/{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)


    def upload_file(self, filename):
        path = 'hrm/file/{}'.format(filename)
        return path

    reume = models.ImageField(upload_to=upload_file, null=True, blank=True)

    def __str__(self):
        return f"{self.eid}"