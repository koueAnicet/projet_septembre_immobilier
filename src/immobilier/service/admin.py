from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.
from service.models  import *



@admin.register(CategoryProperty)
class CategoryPropertyAdmin(admin.ModelAdmin): 
    list_display=(
        'name',
        )


@admin.register(BedNumber)
class BedNumberAdmin(admin.ModelAdmin): 
    list_display=(
        'interval',
    )

@admin.register(GarageNumber)
class GarageNumberAdmin(admin.ModelAdmin): 
    list_display=(
        'interval',
    )

@admin.register(BathNumber)
class BathNumberAdmin(admin.ModelAdmin): 
    list_display=(
        'interval',
    )
    

      
@admin.register(PriceRangeMin)
class PriceRangeMinAdmin(admin.ModelAdmin): 
    list_display=(
        'interval',
    )
    
@admin.register(PriceRangeMax)
class PriceRangeMaxAdmin(admin.ModelAdmin): 
    list_display=(
        'interval',
    )



@admin.register(AreaProperty)
class AreaPropertyAdmin(admin.ModelAdmin): 
    list_display=(
        'interval',
    )
 
#--------------add after------------#        

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
        'city',
        'status',
        'bed_numbers',
        'bath_numbers',
        'piscine',
        'terrain',
        'cheminer',
        'sortie_secours',
        'jardin',
        'area_numbers',
        'built_in',
        'water_front',
        'accessible_vehicule',
        'child_bredroom',
        'desc_water_front',
        'category_property',
        'image1',
        'image2',
        'image3',
        'image4',
        'videos',
        'videos2',
        'accept_condition',
    )
    search_fields =['status', 'city']
    raw_id_fields=['user_property_submit']
    ordering = ['name']
    @admin.action(description='Mark selected properties as published')
    def make_published(self, request, queryset):
        updated= queryset.update(active=True)
        self.message_user(request, ngettext(
            '%d property was successfully marked as published.',
            '%d properties were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
    actions = [make_published]
    #action = ['active', 'accept_condition']