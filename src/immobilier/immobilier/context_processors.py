from django.shortcuts import render, redirect
from authentication.forms import NewsLetterForm, SubmitProperForm
from service.models import City, SubmitProperty
from web.models import Banner, OtherBanner
from web.models import SiteInfos
from service  import models
from authentication  import models


def get_site_infos(request):
    return ''


def get_site_infos(request):
    return ''



def get_site_infos(request):
    form = NewsLetterForm()
    form2 = SubmitProperForm()

    site_infos=SiteInfos.objects.first()
    all_properties= SubmitProperty.objects.filter(active=True).order_by('created')
    properties_count= SubmitProperty.objects.all().count()
    banner = Banner.objects.first()
 
    city = City.objects.all().count()

    return {
        'site_infos': site_infos,
        'all_properties': all_properties,
        'properties_count': properties_count,
        'city': city,
        'banner':  banner,
        'form':  form,
        'form2':  form2,
        }


def get_search_property(request):
    class_form = NewsLetterForm
    class_form2 = SubmitProperForm
    
    try:
        if request.method == 'GET':
            form = class_form()
            form2 = class_form2()
            
            other_banner = OtherBanner.objects.filter(active=True)
            site_infos = SiteInfos.objects.first()
            banner = Banner.objects.first()
            
            all_properties= SubmitProperty.objects.filter(active=True).order_by('created')
            properties_count= SubmitProperty.objects.all().count()
            city = City.objects.all().count()
            
            # faire un choix de 4 elements   
            all_request_data = request.GET
            print('rghgh', all_request_data) 
            all_house = models.SubmitProperty.objects.filter(active=True)
            
            #word = request.GET["word"]
            name = all_request_data.get("name")
            # city = request.GET["city"]
            status = all_request_data.get("status")
            bed_numbers = request.GET("bed_numbers")
            bath_numbers = request.GET("bath_numbers")
            area_numbers = request.GET("area_numbers")
            price_range_min = request.GET("price_range_min")
            price_range_max = request.GET("price_range_max")
            piscine = request.GET("piscine")
            terrain = request.GET("terrain")
            jardin = request.GET("jardin")
            garage_number = request.GET("garage_number")
            
            # if city and int(city) != -1:
            #     all_house = all_house.filter(city__id = int(city))
            
            if status and int(status) != 1:
                all_house = all_house.filter(status__id = int(status))
            
            if name and int(name) != 1:
                all_house = all_house.filter(name__id = int(name))
            
            if bed_numbers and int(bed_numbers) != 1:
                all_house = all_house.filter(bed_numbers__id = int(bed_numbers))
            
            if bath_numbers and int(bath_numbers) != 1:
                    all_house = all_house.filter(bath_numbers__id = int(bath_numbers))
            
            if area_numbers and int(area_numbers) != 1:
                    all_house = all_house.filter(area_numbers__id = int(area_numbers))
            
            if price_range_min and int(price_range_min) != 1:
                    all_house = all_house.filter(rice_range_min__id = int(price_range_min))
            
            if price_range_max and int(price_range_max) != 1:
                    all_house = all_house.filter(rice_range_max__id = int(price_range_max))
            
            if piscine and int(piscine) != 1:
                    all_house = all_house.filter(piscine__id = int(piscine))
            
            if terrain and int(terrain) != 1:
                    all_house = all_house.filter(terrain__id = int(terrain))
            
            if jardin and int(jardin) != 1:
                    all_house = all_house.filter(jardin__id = int(jardin))
            
            if garage_number and int(garage_number) != 1:
                    all_house = all_house.filter(garage_number__id = int(garage_number))
            
            data = {
                        "houses": all_house
                    }
            
            return  {
                'all_properties':  data,
                'form':  form,
                'form2':  form2,
                'site_infos':  site_infos,
                'banner':  banner,
                'properties_count':  properties_count,
                'city':  city,
            }
    
    except Exception as e:
        print("Exception ",str(e))
        
    return ''

