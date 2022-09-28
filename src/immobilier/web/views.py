from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View

from authentication.forms import ContactForm, NewsLetterForm

from web.models import OtherBanner,Banner, SiteInfos,NewsLetter
from authentication.forms import TestimonialForm

class HomeView(View):
    templates_name="web/pages/index.html"
          
    def get(self, request):
        
        # banner = Banner.objects.filter(active=True)
        # other_banner = OtherBanner.objects.filter(active=True)
        site_infos = SiteInfos.objects.filter(active=True)
        return render(request, self.templates_name, locals())
    
    # def post(self, request):
    #     form = self.class_from(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Email envoyé avec succes.')
    #     return render(request, self.templates_name, locals())
    
    
class TestimonialView(View):
    templates_name="web/pages/single.html"
    class_form = TestimonialForm

    def get(self):
        pass 
    def post(self, request):

        form = self.class_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre commentaire a été enregistré avec succes!")
            return redirect('single-property')
        else:
            messages.error(request, "Votre commentaire n'a pu être enregistré!")
            
        return render (request, self.template_name, locals()) 
    

class ContactView(View):
    template_name="web/pages/contact.html"
    class_form = ContactForm
    
    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message envoyé avec sucess.')
            return redirect('home')  
        else:
            messages.error(request, 'Message a échoué')
        return render(request, self.template_name , locals())

def send_news_letter(request):
    return render(request, )      

class NewsLetterView(View):
    templates_name="web/pages/index.html"
    class_from = NewsLetterForm        
    # def get(self, request):
    #     form = self.class_from()
    #     # banner = Banner.objects.filter(active=True)
    #     # other_banner = OtherBanner.objects.filter(active=True)
    #     site_infos = SiteInfos.objects.filter(active=True)
    #     return render(request, self.templates_name, locals())
    
    def post(self, request):
        form = self.class_from(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email envoyé avec succes.')
        return render(request, self.templates_name, locals())
    
