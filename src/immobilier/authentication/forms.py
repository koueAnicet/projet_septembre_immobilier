from email import message
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth import get_user_model
from authentication.models import User

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
        
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = models.NewsLetter
        fields=[
            'email',
        ]
class SubmitProperForm(forms.ModelForm):
    class Meta:
        model = service_models.SubmitProperty
        fields= [
            'image_first',
            'name',
            'price',
            'description',
            'state',
            'city',
            'status',
            'image1',
            'image2',
            'image3',
            'image4',
            'videos',
            'videos2',
            'accept_condition',
        ]