
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class RepeatFields(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
       
class TypePiece(RepeatFields):
    name = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.name

class InfoPiece(RepeatFields):
    type_piece = models.ForeignKey(
        TypePiece,
        on_delete=models.SET_NULL,
        null=True,
        related_name="type_piece"
    )
    number = models.CharField(max_length=150, blank=True)
    photo_front = models.ImageField(blank=True, null=True)
    photo_back = models.ImageField(blank=True, null=True)
    def __str__(self) -> str:
        return self.number

class Country(RepeatFields):
    name = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.name
    
class Nationality(RepeatFields):
    name = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.name
class Social_link(RepeatFields):
    name = models.CharField(max_length=30)
    icon = models.TextField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name
    
class User(AbstractUser, RepeatFields):
    photo =models.FileField()
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
    def __str__(self):
        return self.username