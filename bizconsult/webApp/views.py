from codecs import Codec
from django.shortcuts import render
from webApp.models import*
from serviceConseilApp.models import*
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    site_info = Site_info.objects.first()
    banner = Banner.objects.first()
    social_network = Social_Network.objects.all()
    potentialite = Potentialite.objects.all()
    feature = Feature.objects.first()
    about = About.objects.first()
    service = Service.objects.all()
    team =Team.objects.all()
    testimonials = Testimonial.objects.all()
    team_network = Reseau_social_team.objects.all()
    potentialites = Potentialite.objects.all()

    return render(request, 'bizconsult/index.html', locals())
def home(request):
    return render(request, 'bizconsult/home.html', locals())
def about(request):
    return render(request, 'bizconsult/about.html', locals())
def contact(request):
    return render(request, 'bizconsult/contact.html', locals())
def quote(request):
    return render(request, 'bizconsult/quote.html', locals())
def service(request):
    return render(request, 'bizconsult/service.html', locals())
def team(request):
    return render(request, 'bizconsult/team.html', locals())
def testimonial(request):
    return render(request, 'bizconsult/testimonial.html', locals())
def feature(request):
    return render(request, 'bizconsult/feature.html', locals())
def error_404(request):
    return render(request, 'bizconsult/404.html', locals())

#get informations in contact
def get_info_contact(request):
    alert =""
    success = True
    if request.method == "POST":
        name_contact = request.POST.get('name')
        email_contact = request.POST.get('email')
        subjects_contact = request.POST.get('name')
        comments_contact = request.POST.get('name')
        contact = Contact(id_name=name_contact, id_email=email_contact, id_subjects=subjects_contact, id_message=comments_contact)
        contact.save()

        alert = 'enregistrement reuissir'
    
    data = {
        'alert': alert,
        'success': success
    }
    return JsonResponse(data, safe=False)