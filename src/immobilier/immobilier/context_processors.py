from web.models import SiteInfos
from service  import models
from authentication  import models


def get_site_infos(request):
    return ''


def get_site_infos(request):
    return ''



def get_site_infos(request)-> dict:
    site_infos=SiteInfos.objects.filter(active=True)
    return {'site_infos': site_infos}