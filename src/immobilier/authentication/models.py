from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class RepeatFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        

       
class TypePiece(RepeatFields):
    name = models.CharField(max_length=150)


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


class Country(RepeatFields):
    name = models.CharField(max_length=150)


class Nationality(RepeatFields):
    name = models.CharField(max_length=150)


class User(AbstractUser):
    
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
        related_name="info_piece",
    )
    