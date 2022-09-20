
from django.contrib import admin
from django.urls import path, include

from web import views 


urlpatterns = [

    path('',views.HomeView.as_view(), name="home"),

    
]
