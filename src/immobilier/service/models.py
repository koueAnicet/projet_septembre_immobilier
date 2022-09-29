from django.contrib.auth import get_user_model
from django.db import models
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField


class StatusProperty(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'StatusProperty'
        managed = True
        verbose_name = 'StatusProperty'
        verbose_name_plural = 'StatusProperties'

class State(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'State'
        managed = True
        verbose_name = 'State'
        verbose_name_plural = 'States'
    def __str__(self):
        return self.name


class City(models.Model):
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



class SubmitProperty(models.Model):
    user_property_submit = get_user_model()
    image_first = models.FileField(upload_to='image_first')
    name=models.CharField(max_length=150, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    phone = PhoneNumberField(region="CI", blank=True, null=True)
    description =HTMLField(blank=True, null=True)
    state = models.ForeignKey(
        State,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='property_state',
    )
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
    bed_numbers=models.PositiveBigIntegerField(blank=True, null=True)
    bath_numbers=models.PositiveBigIntegerField(blank=True, null=True)
    area_numbers=models.PositiveBigIntegerField(blank=True, null=True)
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
