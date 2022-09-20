from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class HomeView(View):
    templates_name="web/pages/index.html"
    def get(self, request):
        return render(request, self.templates_name, locals())
    
    def post(self, request):
        pass
    
    
 