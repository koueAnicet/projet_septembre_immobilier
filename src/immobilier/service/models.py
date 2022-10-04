from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField

from authentication.models import User
from authentication.models import FieldsDate


class CategoryProperty(FieldsDate):
    name = models.CharField(max_length=50)
    def __str__(self):
            return self.name
    class Meta:
        db_table = 'CategoryProperty'
        managed = True
        verbose_name = 'CategoryProperty'
        verbose_name_plural = 'CategoryProerties'
    
    
class BedNumber(FieldsDate):  #lit 
    interval = models.PositiveBigIntegerField()
    

    
    
class GarageNumber(FieldsDate):  
    interval = models.PositiveBigIntegerField(blank=True, null=True)   
    
    
      
class BathNumber(FieldsDate):  #salle de bain     
    interval = models.PositiveBigIntegerField()
   


     

class PriceRangeMin(FieldsDate):#grille de prix
    interval = models.PositiveBigIntegerField()
    
    
    
class PriceRangeMax(FieldsDate):#grille de prix
    interval = models.PositiveBigIntegerField()
    

class AreaProperty(FieldsDate):
    interval = models.PositiveSmallIntegerField()   
    
    
    
class StatusProperty(FieldsDate):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'StatusProperty'
        managed = True
        verbose_name = 'StatusProperty'
        verbose_name_plural = 'StatusProperties'


class State(FieldsDate):
    name = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'State'
        managed = True
        verbose_name = 'State'
        verbose_name_plural = 'States'
        
    def __str__(self):
        return self.name


class City(FieldsDate):
    state = models.ForeignKey(
        State,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='properti_state',
        
    )
    name = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'City'
        managed = True
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
    def __str__(self):
        return self.name


class SubmitProperty(FieldsDate):
    user_property_submit = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='submit_user',
        null=True
    )
    image_first = models.FileField(upload_to='image_first')
    name=models.CharField(max_length=150, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    phone = PhoneNumberField(region="CI", blank=True, null=True)
    description =HTMLField(blank=True, null=True)
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_city',
    )
    status = models.ForeignKey(
        StatusProperty,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_status',
    )
    bed_numbers = models.ForeignKey(
        BedNumber,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_bed',
    )
    bath_numbers = models.ForeignKey(
        BathNumber,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_bath',
    )
    area_numbers = models.ForeignKey(
        AreaProperty,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_area',
    )
    price_range = models.ForeignKey(
        PriceRangeMin,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_price',
    )
    price_range = models.ForeignKey(
        PriceRangeMax,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_price',
    )
    
    piscine = models.BooleanField(default=False)
    terrain = models.BooleanField(default=False)
    cheminer=models.BooleanField(default=False)
    sortie_secours=models.BooleanField(default=False)
    jardin=models.BooleanField(default=False)
    garage_number = models.ForeignKey(
        GarageNumber,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_Garage',
    )
  
    category_property= models.ForeignKey(
        CategoryProperty,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_category',
    )
    #----infos additional--#
    built_in = models.PositiveIntegerField(max_length=4,  blank=True, null=True)
    water_front = models.BooleanField(default=False)#bordure eau
    accessible_vehicule = models.BooleanField(default=False)#bordure eau
    child_bredroom = models.BooleanField(default=False)#chambre enfant
    desc_water_front =HTMLField(blank=True, null=True)
    image1 = models.ImageField(upload_to='img1',blank=True, null=True)
    image2 = models.ImageField(upload_to='img2',blank=True, null=True)
    image3 = models.ImageField(upload_to='img3',blank=True, null=True)
    image4 = models.ImageField(upload_to='img4',blank=True, null=True)
    videos = models.URLField(blank=True, null=True)
    videos2 = models.ImageField(upload_to='videos2', blank=True, null=True)
    accept_condition = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    
    class Meta:
        db_table = 'SubmitProperty'
        managed = True
        verbose_name = 'SubmitProperty'
        verbose_name_plural = 'SubmitProperties'
