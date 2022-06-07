from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('home/',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('quote/',views.quote, name="quote"),
    path('service/',views.service, name="service"),
    path('feature/',views.feature, name="feature"),
    path('team/',views.team, name="team"),
    path('testimonial/',views.testimonial, name="testimonial"),
    path('error_404',views.error_404, name="404"),
]