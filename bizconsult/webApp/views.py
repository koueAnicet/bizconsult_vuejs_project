from django.shortcuts import render

# Create your views here.

def index(request):
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