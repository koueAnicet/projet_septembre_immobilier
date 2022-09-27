from tinymce.models import HTMLField
from django.db import models
from django.core.exceptions import ValidationError
from authentication.models import FieldsDate

class OtherBanner(FieldsDate):
    other_image_banner = models.ImageField(upload_to='other_img')


class Banner(FieldsDate):
    title = models.CharField( max_length=150)
    description = HTMLField()
    def __str__(self):
        return self.description


class NewsLetter(FieldsDate):
    email = models.EmailField( max_length=150)
    # def __str__(self):
    #     return self.email
    
class SocialLinks(FieldsDate):
    name= models.CharField(max_length=150)
    icon =  models.CharField(max_length=150)
    link = models.URLField(max_length=255)
    def __str__(self):
        return self.name
        
    
class SiteInfos(FieldsDate):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    emails = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Testimonial(FieldsDate):
    name = models.CharField(max_length=150)
    emails = models.EmailField(max_length=255)
    comments = HTMLField()
    def __str__(self):
        return self.name
    
    
class Contact(FieldsDate):
    first_name=models.CharField(max_length=150,)
    last_name=models.CharField(max_length=150, )
    email=models.EmailField(max_length=150, )
    subject=models.CharField(max_length=150)
    message= HTMLField()
    
    def validate_first_name(self):
        if not self.first_name.isalpha() or not self.first_name.isalnum():
            raise ValidationError('Cet champ doit être alphabetique ou alphanumerique')  
        return self.first_name
    
    def validate_first_name(self):
        if not self.last_name.isalpha() or not self.last_name.isalnum():
            raise ValidationError('Cet champ doit être alphabetique ou alphanumerique')  
        return self.last_name