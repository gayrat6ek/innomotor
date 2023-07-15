from django.contrib import admin
from .models import TransportType,CarModel,Brochure,ColorCar,CarInfo,CarInfoChild
# Register your models here.

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['cartype','car_model','price','currency']

class BrochureAdmin(admin.ModelAdmin):
    list_display = ['carmodel','brochure_title']
class ColorCarAdmin(admin.ModelAdmin):
    list_display = ['brochure','color']
class CarInfoAdmin(admin.ModelAdmin):
    list_display = ['title','car_model']

class CarInfoChildAdmin(admin.ModelAdmin):
    list_display = ['title','carinfo']


admin.site.register(CarModel,CarModelAdmin)
admin.site.register(Brochure,BrochureAdmin)
admin.site.register(ColorCar,ColorCarAdmin)
admin.site.register(CarInfo,CarInfoAdmin)
admin.site.register(CarInfoChild,CarInfoChildAdmin)
admin.site.register(TransportType)