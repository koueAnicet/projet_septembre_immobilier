from django.contrib import admin

from authentication.models import User,TypePiece ,InfoPiece ,Country ,Nationality, Social_link
from django.utils.safestring import mark_safe

# Register your models here.



@admin.register(TypePiece)
class AdminTypePiece(admin.ModelAdmin):
    list_display=(
        'name', 
    )
    
    
    
@admin.register(InfoPiece)
class AdminInfoPiece(admin.ModelAdmin):
    list_display=(
        'type_piece',
        'number',
        'photo_front',
        'photo_back',
        'active',
    )
    
    
@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display=(
        'name', 
    )
    
    
@admin.register(Nationality)
class AdminNationality(admin.ModelAdmin):
    list_display=(
        'name',
    )
    
    
@admin.register(Social_link)
class AdminSocial_link(admin.ModelAdmin):
    list_display=(
        'name',
        'icon',
        'link', 
    )
    
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=(
        'photo', 
        'username',
        'first_name',
        'last_name',
        'number_phone',
        'number_phone_two',
        'email',
        'nationality',
        'is_estate_agent',
        'social_link',
        
    )
    search_fields =['username', 'first_name', 'last_name', 'number_phone']
    
    def img_about(self, obj): 
        return mark_safe(f'<img src="{obj.photo.url}" style="height:100px; width:200px">')
