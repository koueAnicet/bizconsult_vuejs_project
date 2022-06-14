from codecs import Codec
from django.shortcuts import render, redirect
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
    alert =""
    success = True

    if request.method == "GET":
        return render(request, 'bizconsult/contact.html', locals())
    else:
        name_contact = request.POST.get('name')
        email_contact = request.POST.get('email')
        subjects_contact = request.POST.get('subjects')
        comment_contact = request.POST.get('message')
        contact = Contact.objects.create(name_contact=name_contact, email_contact=email_contact, subject_contact = subjects_contact, comments_contact=comment_contact)

        alert = 'enregistrement reuissit!'
    
        data = {
        'alert': alert,
        'success': success
        }

        return redirect("contact",data)

    


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
