
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class FieldsDate(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
       
class TypePiece(FieldsDate):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class InfoPiece(FieldsDate):
    type_piece = models.ForeignKey(
        TypePiece,
        on_delete=models.SET_NULL,
        null=True,
        related_name="type_piece"
    )
    number = models.CharField(max_length=150, blank=True)
    photo_front = models.ImageField(blank=True, null=True)
    photo_back = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.number

class Country(FieldsDate):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
    
class Nationality(FieldsDate):
    contry = models.ForeignKey(
        Country, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
    
class Social_link(FieldsDate):
    name = models.CharField(max_length=30)
    icon = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name
    
    
class User(AbstractUser, FieldsDate):
    photo =models.FileField(upload_to="User_photo")
    is_estate_agent= models.BooleanField(default=False)
    number_phone = PhoneNumberField(region="CI")
    number_phone_two = PhoneNumberField(region="CI")
    address = models.CharField(max_length=150, blank=True)
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_nationality",
    )
    info_piece = models.ManyToManyField(
        InfoPiece,
        related_name="user_info_piece",
    )
    social_link = models.ForeignKey(
        Social_link,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_social_link"
    )
    description_agent_estate= models.CharField(max_length=1000 , blank=True, null=True)
    def __str__(self):
        return self.username