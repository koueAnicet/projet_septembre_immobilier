
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from authentication import forms
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from immobilier import settings
from web.models import SiteInfos
from service.models import SubmitProperty
from .tokens import generate_token
from authentication.forms import User, VisitorEmailForm

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
        
        if form.is_valid():
            
            form.is_active = False
           
            user = form.save()
            
            login(request, user)
            messages.success(request, "Votre compte a été créé avec success! Nous vous avons envoyez un email de confirmation,veuillez le confirmé")
            
            #Email de bienvenu
            
            subject = "Bienvenue sur ANICK DELACOSTE ESTATE!!"
            message = "Hello "+ user.first_name + "!!\n" + "Bienvenue à ANICK DELACOSTE ESTATE!!\n Merci pour la visite sur notre site web\n Nous t'avons envoyé un email de confirmation, s'il vous plait confirmez votre adresse email afin d'activer votre compte.\n\n Nous vous remercions\n GARO ESTATE TEAM\n"
            from_email = settings.EMAIL_HOST_USER
            to_list =[user.email]#on peu envoyer a plusier personne
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            
            #confirmation d'email
            
            current_site = get_current_site(request)
            email_subject = "Confirmation de l'email " + user.email + "GARO ESTATE - Django Login!!"
            message2 = render_to_string('authentication/pages/email_confirmation.html',{
                'name' : user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            email.fail_silently = False
            email.send()
            
            
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, locals())
    
    
class  LoginView(View):
    template_name = "authentication/pages/login.html" 
    class_form = forms.LoginForm
    
    
    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, locals())
    
    #@method_decorator(login_required)
    def post(self, request):
        form = self.class_form(request.POST)
        
        if form.is_valid():
            #recuperation des infos
            user= authenticate(request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            my_user= User.objects.get(username=user.username)
            if user is not None:
                if user.is_estate_agent and user.is_active != False:
                    
                    login(request, user)
                    fname = user.username
                    messages.success(request, "Bienvenue , vous êtes connecté.")
                    
                    return redirect('user-property')
                elif my_user.is_active==False:
                    messages.error(request, "Vous n'avez pas confirmé votre adresse email , merci de le faire.")
                    
                elif user and user.is_superuser:
                    login(request, user)
                    fname = user.get_full_name
                  
                    #messages.success(request, "f Bonjour {fname}! Merci d'avoir d'être connecté.")
                    return redirect('submit-property')
                
                else:
                    messages.error(request, "Votre adresse email doit être confirmer avant de vous connecter, merci!")
                    
                    return render(request, self.template_name, locals())
        messages.error(request, "Utilisateur introuvable.")
        return render(request, self.template_name, context={'form': form})


class Contact(View):
    template_name=''
    class_form = forms.ContactForm
    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, locals())



class UserProfiles(LoginRequiredMixin,View):
    class_form = forms.NewsLetterForm
    template_name="authentication/pages/user-profile.html"
    
    def get(self, request):
        form = self.class_form()
        
        return render(request, "authentication/pages/user-profile.html", locals())
    
    def post(self, request):
        
        return render(request, "authentication/pages/user-profile.html", locals())

#@login_required

class UserPropertyView(LoginRequiredMixin,View):
    template_name='authentication/pages/user-properties.html'
    class_form = forms.NewsLetterForm


    def get(self, request):
        form = self.class_form()
        # count_bed = SubmitProperty.objects.filter(active=True).count()
        
        AllProperties= SubmitProperty.objects.all()
        paginator = Paginator(AllProperties, 2)
        page_number = request.GET.get('page')
        
        page_obj = paginator.get_page(page_number)
        
        site_infos = SiteInfos.objects.first()
        # count_shaweds = SubmitProperty.objects.filter(active=True).count()
        return render(request, self.template_name,locals())

    def post(self, request):
        
        return redirect('user-profiles')



class SubmitPropertyView(LoginRequiredMixin, View):
    template_name='authentication/pages/submit-property.html'
    form_class= forms.SubmitProperForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, locals())
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            #attente d'user
            f = form.save(commit=False)

            f.user_property_submit = request.user 
            f.save()
            
            return redirect('user-properties')
        
        return render(request, self.template_name, locals())
        
        
class DetailPropertyView(View):
    template_name="authentication/pages/property.html"
    class_form = forms.NewsLetterForm
    class_form2 = forms.VisitorEmailForm
    
    def get(self, request, property):
        form = self.class_form()
        form2 = self.class_form2()
        
        property_index = SubmitProperty.objects.get(id=property)
        return render(request, self.template_name, locals())

    def post(self, request, property):
        
        property_index = SubmitProperty.objects.get(id=property)
        print('ggggg', property_index)
        form2 = self.class_form2(request.POST)
        print('ggggg', form2.phonevisitor)
        if form2.is_valid():
            #ontacter argent par Email
                    
            subject = "Bienvenue sur ANICK DELACOSTE ESTATE!!"
            message = f"Bonjour monsieur  {property_index.user_property_submit}!!\n Je suis interessé par cette maison ci :\n Nom propriété:  {property_index.name} \n Nom propriété: { property_index.area_numbers} \n Prix propriété:  {property_index.price} \n { property_index.area_numbers} \n Merci "
            print('')
            from_email = form2.emailvisitor
            to_list =[property_index.user_property_submit.email]#on peu envoyer a plusier personne
            send_mail(subject, message, from_email, to_list, fail_silently=False)
           
            form2.save()
            messages.success(request, 'Votre message a été envoyé avec succès')
            return redirect('detail-property')
        else:
            messages.error(request, "Votre message n'a été envoyé")
            return redirect('detail-property') 
   
        #info_house= SubmitProperty.objects.get_or_404(pk=id_house)
        return render(request, self.template_name, locals())



class  AllPropertiesView(View):
    template_name='authentication/pages/properties.html'
    class_form = forms.NewsLetterForm
    def get(self, request):
        form = self.class_form()
        all_properties= SubmitProperty.objects.filter(active=True).order_by('created')
        
        paginator = Paginator(all_properties, 6)
        page_number = request.GET.get('page')
        
        page_obj = paginator.get_page(page_number)
        site_infos = SiteInfos.objects.first()
        return render(request, self.template_name, locals())
    def post(self, request):
        
        #all_properties_db = SubmitProperty.objects.filter(active=True)
        return render(request, self.template_name, locals())



#suppression de property
@login_required
def delete_property( request, delete_id):
    template_name='authentication/pages/delete-property.html'
    delete_property = SubmitProperty.objects.get(pk=delete_id)
    if request.method == 'POST':
        delete_property.delete()
        messages.success(request, 'Votre propriété a été supprimée avec succes.')
        return redirect('user-properties')
    return render(request, template_name, locals())


#update property
@login_required
def update_property(request, update_id):
    template_name='authentication/pages/submit-property.html'
    property_update = SubmitProperty.objects.get(pk=update_id)
   
    form= forms.SubmitProperForm(instance=property_update)
    
    if request.method == 'POST':
        form = forms.SubmitProperForm(request.POST ,  request.FILES, instance=property_update)
        
        if form.is_valid():
            form.save() 
            messages.success(request, 'Votre propriété a été modifier avec succès')
            return redirect('detail-property', property_update.id)
    return render(request, template_name , locals())

#ontacter argent
def conatact_agent(request):
    #Email de bienvenu
            
    subject = "Bienvenue sur ANICK DELACOSTE ESTATE!!"
    message = "Hello "+ user.first_name + "!!\n" + "Bienvenue à ANICK DELACOSTE ESTATE!!\n Merci pour la visite sur notre site web\n Nous t'avons envoyé un email de confirmation, s'il vous plait confirmez votre adresse email afin d'activer votre compte.\n\n Nous vous remercions\n GARO ESTATE TEAM\n"
    from_email = settings.EMAIL_HOST_USER
    to_list =[user.email]#on peu envoyer a plusier personne
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    return ''
   
#vue de confirmation email avec token
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=uid)
    except (TypeError,ValueError, OverflowError, User.DoesNotExist):
        user= None
        
    if user is not None and generate_token.check_token(user, token):
        user.is_active =True
        user.save()
        messages.success(request, "Votre compte est activé ,connectez vous maintenant!! ")
        #login(request, user)
        return redirect('home')
    else:
        #messages.error(request, " Ooop, activation a échoué !!!!")
        return render(request, 'authentication/pages/activation_echoue.html', locals())