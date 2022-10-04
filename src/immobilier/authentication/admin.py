from django.contrib import admin

from authentication.models import User
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=(
        'username',
        'first_name',
        'last_name',
        'number_phone',
        'number_phone_two',
        'email',
        'nationality',
        'is_estate_agent',
        'social_link',
        'photo', 
    )
    search_fields =['username', 'first_name', 'last_name', 'number_phone']
    
    def image_agent(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="height:100px; width:200px">')