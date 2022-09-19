from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class HomeView(View):
    templates_name="immoblier/pages/"
    form = ''
    
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    
    
 