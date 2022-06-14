from webApp.models import Site_info

def global_Site_info(request):

    site = Site_info.objects.all()
    return {
        "site_info": site,
    }