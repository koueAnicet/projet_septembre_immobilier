from email import message
from django.shortcuts import render, redirect
from django.views.generic import View
from immobilier.web.models import OtherBanner,Banner, SiteInfos
from authentication.forms import TestimonialForm


class HomeView(View):
    templates_name="web/pages/index.html"
    
        
    def get(self, request):
        banner = Banner.objects.filter(active=True)
        other_banner = OtherBanner.objects.filter(active=True)
        site_infos = SiteInfos.objects.filter(active=True)
        return render(request, self.templates_name, locals())
    
    def post(self, request):
        #traiment sendd email
        pass

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
            return redirect('single-property')
        return render (request, self.template_name, locals()) 
    
 