from django.contrib import admin

# Register your models here.
from service.models  import *


@admin.register(StatusProperty)
class StatusPropertyAdmin(admin.ModelAdmin): 
    list_display=(
        'name',
        )
    
@admin.register(State)
class StateAdmin(admin.ModelAdmin): 
    list_display=(
        'name',
        
        )
@admin.register(City)
class CityAdmin(admin.ModelAdmin): 
    list_display=(
        'state',
        'name',
        )
@admin.register(SubmitProperty)
class SubmitPropertyAdmin(admin.ModelAdmin): 
    list_display=(
        'user_property_submit',
        'image_first',
        'name',
        'price',
        'phone',
        'description',
        'status',
        'city',
        'status',
        'bed_numbers',
        'bath_numbers',
        'area_numbers',
        'image1',
        'image2',
        'image3',
        'image4',
        'videos',
        'videos2',
        'accept_condition',
    )