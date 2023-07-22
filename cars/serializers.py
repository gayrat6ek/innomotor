from rest_framework import serializers
from .models import TransportType,CarInfo,CarInfoChild,CarModel,Brochure,ColorCar,UserInfo

class GetAdvertSerializer(serializers.ModelSerializer):
    car_image = serializers.CharField(source = 'car_image.url')
    class Meta:
        model = CarModel
        fields = ['pk','car_image','price','currency','car_model','title']


class GetCarImageFromColorSer(serializers.ModelSerializer):
    car_model = serializers.CharField(source='brochure.carmodel.car_model')
    price = serializers.CharField(source='brochure.carmodel.price')
    currency = serializers.CharField(source= 'brochure.carmodel.currency')
    cartype = serializers.CharField(source='brochure.carmodel.cartype.title')
    car_image = serializers.CharField(source='car_image.url')
    car_id = serializers.IntegerField(source='brochure.carmodel.pk')
    class Meta:
        model = ColorCar
        fields = ['car_image','car_model','price','currency','cartype','car_id']


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportType
        fields = ['title','id']



class GetFromCarModelSer(serializers.ModelSerializer):
    car_image =serializers.CharField(source='car_image.url')
    class Meta:
        model = CarModel
        fields = ['pk','title','car_model','car_description','car_image']

class CarInfoChildSer(serializers.ModelSerializer):
    class Meta:
        model = CarInfoChild
        fields = ['pk','title','image','imagetext']

class CarInfoSer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = ['pk','title','slug','full_info']



class ColorsCarSer(serializers.ModelSerializer):
    class Meta:
        model = ColorCar
        fields = ['pk','color','car_image']


class BrochureCarSer(serializers.ModelSerializer):
    class Meta:
        model = Brochure
        fields = ['pk','brochure','brochure_title']


class UserInfoSer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['full_name','phone_number','question']