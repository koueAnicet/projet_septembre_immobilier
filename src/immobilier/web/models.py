from distutils.command.upload import upload
import email
from django.db import models



class OtherBanner(models.Model):
    other_image_banner = models.ImageField(upload_to='other_img')


class Banner(models.Model):
    title = models.CharField( max_length=150)
    description = HTMLField()
    def __str__(self):
        return self.description


class NewsLetter(models.Model):
    email = models.EmailField( max_length=150)

class SocialLinks(models.Model):
    name= models.CharField(max_length=150)
    icon =  models.CharField(max_length=150)
    link = models.URLField(max_length=255)
    def __str__(self):
        return self.name
        
    
class SiteInfos(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    emails = models.EmailField(max_length=255)
    def __str__(self) -> str:
        return self.name
    

class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    emails = models.EmailField(max_length=255)
    comments = HTMLField()
    def __str__(self) -> str:
        return self.name