from django.urls import path
from .views import GetAdView,GetImageFromColor,FilterCarByTypeView,GetFromCarModelVeiw,GetFullDataView,UserInfoView

urlpatterns = [
    path('get/ad/all',GetAdView.as_view()),
    path('get/filter/cars',GetImageFromColor.as_view()),
    path('filter/car/by/type/<int:id>',FilterCarByTypeView.as_view()),
    path('get/cars/last/section',GetFromCarModelVeiw.as_view()),
    path('full/data/car/<int:id>',GetFullDataView.as_view()),
    path('user/question',UserInfoView.as_view())
]