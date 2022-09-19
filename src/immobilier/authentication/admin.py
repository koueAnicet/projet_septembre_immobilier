from django.contrib import admin

from authentication.models import User
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=(
        'photo',
        'username',
        'first_name',
        'last_name',
        'number_phone',
        'number_phone_two',
        'address',
        'nationality',
        'is_estate_agent',
        'social_link',
        
        
    )
    def image_agent(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="height:100px; width:200px">')