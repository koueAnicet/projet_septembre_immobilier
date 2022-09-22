from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth import get_user_model
from authentication.models import User


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
            "email", "username", 
            "number_phone",  
            "number_phone_two",  
            "nationality", 
            "address", 
            'social_link',
            'info_piece'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label=" Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')