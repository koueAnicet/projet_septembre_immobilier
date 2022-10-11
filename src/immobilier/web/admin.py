from django.contrib import admin
from web.models import *



@admin.register(OtherBanner)
class OtherBannerAdmin(admin.ModelAdmin): 
    list_display=(
        'other_image_banner',
    )
        
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin): 
    list_display=(
        'title',
        'slide_1',
        'slide_2',
        'slide_3',
        'description',
    )
   
@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin): 
    list_display=(
        'email',
    )

@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin): 
    list_display=(
        'name',
        'icon',
        'link',
    )
    
@admin.register(SiteInfos)
class SiteInfosAdmin(admin.ModelAdmin): 
    list_display=(
        'name',
        'contact',
        'address',
        'emails',
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin): 
    list_display=(
        'name',
        'emails',
        'comments',
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin): 
    list_display=(
        'first_name',
        'last_name',
        'email',
        'subject',
        'message',
    )
       
    
    