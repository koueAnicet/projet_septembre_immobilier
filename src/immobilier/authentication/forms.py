from email import message
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField

from django.contrib.auth import get_user_model
from authentication.models import User
from service.models import SubmitProperty

from web import models
from service import models as service_models


class FormRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            
            "last_name", 
            "first_name", 
            "email", 
            "number_phone",
            "username",
            "is_estate_agent",
        ]
        
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "last_name", 
            "first_name", 
            "email", 
            "username", 
            "number_phone",  
            "number_phone_two",  
            "nationality", 
            "address", 
            'social_link',
            'info_piece'
        ]

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = models.Testimonial
        fields=[
            'name',
            'emails',
            'comments',
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label=" Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields=[
            'first_name',
            'last_name',
            'email',
            'subject',
            'message',
        ]
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha() or not first_name.isalnum():
           raise ValidationError('Cet champ doit être alphabetique ou alphanumerique.')  
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha() or not last_name.isalnum():
            raise ValidationError('Cet champ doit être alphabetique ou alphanumerique.')  
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email or not email:
            raise ValidationError('Enytrez un email valide.')  
        return email
    
    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if not subject.isalpha() or not subject.isalnum():
            raise ValidationError('Cet champ doit être alphabetique ou alphanumerique.')  
        return subject

    def clean_message(self):
        message = self.cleaned_data['message']
        if not message:
            raise ValidationError('Cet champ doit pas être vide.')  
        return message

        
        
class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = models.NewsLetter
        fields=[
            'email',
        ]
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email or not email:
            raise ValidationError('Enytrez un email valide.')  
        return email
    
    
# class SubmitProperForm(forms.Form):
#     image_first = forms.FileField()
#     name=forms.CharField(max_length=150)
#     price = forms.IntegerField()
#     phone = forms.IntegerField(widget=forms.NumberInput())
#     description =HTMLField()
#     image1 = forms.ImageField()
#     image2 = forms.ImageField()
#     image3 = forms.ImageField()
#     image4 = forms.ImageField()
#     videos = forms.URLField()
#     videos2 = forms.ImageField()
#     accept_condition = forms.BooleanField()
    
class SubmitProperForm(forms.ModelForm):   
    class Meta:
        model = SubmitProperty
        fields = [
            
            'image_first',
            'name',
            'price',
            'phone',
            'description',
        
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
            
        ]
