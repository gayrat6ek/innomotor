from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import TransportType,CarInfo,CarInfoChild,CarModel,Brochure,ColorCar,UserInfo
from .serializers import GetAdvertSerializer,GetCarImageFromColorSer,CarTypeSerializer,GetFromCarModelSer
from .serializers import CarInfoChildSer,CarInfoSer,ColorsCarSer,BrochureCarSer,UserInfoSer
# Create your views here.



class GetAdView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = GetAdvertSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.data = {'success':True,'allcars':response.data}
        return response


class GetImageFromColor(generics.ListAPIView):
    queryset = ColorCar.objects.all().distinct('brochure_id')
    serializer_class = GetCarImageFromColorSer
    def get(self, request, *args, **kwargs):
        data = super().get(request, *args, **kwargs)
        cartype = TransportType.objects.all()
        typeser = CarTypeSerializer(cartype,many=True)
        data.data = {'allcars':data.data,'cartypes':typeser.data,'success':True}
        return data
    
class FilterCarByTypeView(generics.RetrieveAPIView):
    serializer_class = GetCarImageFromColorSer
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        cars = ColorCar.objects.filter(brochure__carmodel__cartype__id=id).distinct('brochure_id')
        serialiser = self.serializer_class(cars,many=True)
        return Response({'allcars':serialiser.data,'success':True})
    
class GetFromCarModelVeiw(generics.ListAPIView):
    serializer_class = GetFromCarModelSer
    queryset = CarModel.objects.order_by('?')[:6]
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.data = {'success':True,'allcars':response.data}
        return response
    


class GetFullDataView(generics.RetrieveAPIView):
    serializer_class = GetAdvertSerializer
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        car_info = {'cardata':[]}
        carmodel_car = CarModel.objects.get(pk=id)
        brochure_car = Brochure.objects.get(carmodel__id=id)
        car_info['car_model'] = GetFromCarModelSer(carmodel_car).data
        car_info['colors'] = {'brochure':BrochureCarSer(brochure_car).data,'image_color':ColorsCarSer(brochure_car.carcolor.all(),many=True).data}



        carinfodata =CarInfo.objects.filter(car_model = id)
        for i in carinfodata:
            carinfochildservi = CarInfoChildSer(i.carchild.all(),many=True)
            carinfoservi = CarInfoSer(i)
            car_info['cardata'].append({'carinfo':carinfoservi.data,'carinfochild':carinfochildservi.data})
        
        return Response(car_info)
    




class UserInfoView(generics.CreateAPIView):
    serializer_class = UserInfoSer
    queryset  = UserInfo.objects.all()
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data = {'success':True,'data':response.data}
        return response