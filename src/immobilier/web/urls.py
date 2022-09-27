
from django.contrib import admin
from django.urls import path, include

from web import views 


urlpatterns = [

    path('',views.HomeView.as_view(), name="home"),
    path('contact/',views.ContactView.as_view(), name="contact"),
    path('news-letter/',views.NewsLetterView.as_view(), name="news-letter"),
    path('properties/',views.NewsLetterView.as_view(), name="news-letter"),
    
    
]
