from django.db import models
from colorfield.fields import ColorField
# Create your models here.



class TransportType(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class CarModel(models.Model):
    car_model = models.CharField(max_length=200)
    title = models.CharField(max_length=200,null=True)
    car_description = models.TextField(null=True)
    car_image = models.ImageField(upload_to='media')
    price = models.BigIntegerField()
    currency = models.CharField(max_length=244,choices=(('uzs','UZS'),('usd','USD')))
    cartype = models.ForeignKey(TransportType,on_delete=models.CASCADE)
    def __str__(self):
        return self.car_model



class Brochure(models.Model):
    carmodel= models.OneToOneField(CarModel,on_delete=models.CASCADE)
    brochure = models.FileField(upload_to='media')
    brochure_title = models.CharField(max_length=200)
    def __str__(self):
        return self.carmodel.car_model

class ColorCar(models.Model):
    color = ColorField(default='#FF0000')
    car_image = models.ImageField(upload_to='media')
    brochure  = models.ForeignKey(Brochure,on_delete=models.CASCADE,related_name='carcolor')
    def __str__(self):
        return self.brochure.carmodel.car_model
    



class CarInfo(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    full_info = models.TextField()
    car_model = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='carinfo')
    def __str__(self):
        return f"{self.title} - {self.car_model.car_model}"


class CarInfoChild(models.Model):
    title = models.CharField(max_length=200)
    image= models.ImageField(upload_to='media')
    imagetext = models.TextField()
    carinfo = models.ForeignKey(CarInfo,on_delete=models.CASCADE,related_name='carchild')
    def __str__(self):
        return f"{self.carinfo.car_model.car_model} - {self.title}"
    



class UserInfo(models.Model):
    full_name = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
