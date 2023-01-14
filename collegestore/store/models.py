from django.db import models

# Create your models here.
class userData(models.Model):
    name=models.CharField(max_length=250)
    dob = models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=200)
    phone=models.IntegerField()
    mail=models.EmailField()
    address=models.TextField()
    department=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    purpose=models.CharField(max_length=250)
    materials=models.CharField(max_length=500)



