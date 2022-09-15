from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.
def logout_user(request):
    pass


class HomeView(View):
    cform = ''
    
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    
    
    
class  RegisterView(View):
    form = ''
    
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    
    
class  LoginView(View):
    form = ''
    
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    