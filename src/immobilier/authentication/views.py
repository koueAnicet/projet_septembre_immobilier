from tkinter import E
from django.forms import EmailField
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from authentication import forms
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from immobilier import settings
from authentication.tokens import generate_token
from authentication.forms import User


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
            user.is_active = False
            user = form.save()
            
            login(request, user)
            messages.success(request, "Votre compte a été créé avec success! Nous vous avons envoyez un email de confirmation, s'il vous plait veuillez le confirmé")
            
            #Email de bienvenu
            subject = "Bienvenue à GARO ESTATE!!"
            message = "Hello "+ user.first_name + "!!\n" + "Bienvenue à GARO ESTATE!!\n Merci pour la visite sur notre site web\n Nous t'avons envoyé un email de confirmation, s'il vous plait confirmez votre adresse email afin d'activer votre compte.\n\n Nous vous remercions\n Membre d'admin\n"
            from_email = settings.EMAIL_HOST_USER
            to_list =[user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            #confirmation d'email
            
            current_site = get_current_site(request)
            email_subjuct = "Confirmez votre email @ GARO ESTATE - Django Login!!"
            message2 = render_to_string('authentication/pages/email_confirmation.html',{
                'name' : user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email =EmailMessage(
                email_subjuct,
                message2,
                settings.EMAIM_HOST_USER,
                [user.email],
            )
            email.fail_silently = True
            email.send()
            
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

def active(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=uid)
    except (TypeError,ValueError, OverflowError, User.DoesNotExist):
        user= None
        
    if user is not None and generate_token.check_token(user,token):
        user.is_active =True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'authentication/pages/activation_echoue.html', locals())