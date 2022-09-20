from asyncore import read
from django.conf import settings
from django.db import reset_queries
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from authentication import forms


def logout_user_auth(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('home')


   
class  RegisterView(View):
    template_name = "authentication/pages/register.html" 
    class_form = forms.FormRegister 
    
    def get(self, request):
    
        form = self.class_form()
        messages.success(request, "Merci de bien vouloir vous inscris!")
        
        return render(request, self.template_name, locals())
    
    def post(self, request):
        form = self.class_form(request.POST)
        
        if form.is_valid:
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec success!")
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, locals())
    
    
class  LoginView(View):
    template_name = "authentication/pages/login.html" 
    class_form = forms.LoginForm
    
    
    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, locals())
    
    def post(self, request):
        form = self.class_form(request.POST)
        
        if form.is_valid:
            #recuperation des infos
            user= authenticate(request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            
            if user:
                if user.is_estate_agent:
                    login(request, user)
                    fname = user.username
                    messages.success(request, "Merci d'avoir d'être connecté.")
                    
                    return redirect('home',locals())
                elif user and user.is_superuser:
                    login(request, user)
                    fname = user.username
                  
                    messages.success(request, "f Bonjour {fname}! Merci d'avoir d'être connecté.")
                    return redirect('home')
                else:
                    
                    messages.error(request, "Mauvais identifiant")
                    return render(request, self.template_name, locals())
        
        return render(request, self.template_name, locals())


def submit_property(request):
    template_name = "autthentication/pages/submit-property.html"
    #if request.method == 'POST':
    return render(request, template_name, locals())


def user_property(request):
    template_name = "autthentication/pages/user-properties.html"
    return render(request, template_name, locals())