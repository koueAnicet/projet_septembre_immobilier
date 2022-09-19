from django.conf import settings
from django.db import reset_queries
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from authentication import forms


def logout_user(request):
    pass


   
class  RegisterView(View):
    template_name = "authentication/pages/register.html" 
    class_form = forms.FormRegister 
    
    def get(self, request):
        
        form = self.class_form()
        messages.success(request, "Merci de bien vouloir vous inscris!")
        
        return render(request, self.template_name, locals())
    
    def post(self, request):
        form = self.class_form(request.POST)
        print("@-----@----@------@")
        print(form)
        if form.is_valid:
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec success!")
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, locals())
    
    
class  LoginView(View):
    templates = "authentication/pages/login.html" 
    class_form = forms.LoginForm
    
    
    def get(self, request):
        form = self.class_form()
        return render(request, self.templates, locals())
    
    def post(self, request):
        pass
    