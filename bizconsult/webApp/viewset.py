from rest_framework import viewsets
from webApp.serializers import *
from webApp.models import Site_info,Banner,Social_Network,Social_Network,Contact,Potentialite,Feature,About


class SiteInfoViewSet(viewsets.ModelViewSet):
    queryset = Site_info.objects.all()
    serializer_class = SiteInfoSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = Social_Network.objects.all()
    serializer_class = SocialNetworkSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class PotentialiteViewiewSet(viewsets.ModelViewSet):
    queryset = Potentialite.objects.all()
    serializer_class = PotentialiteSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

#-------------service conceil app----------

# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
    
# class TeamViewSet(viewsets.ModelViewSet):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer

# class ReseauSocialTeamViewSet(viewsets.ModelViewSet):
#     queryset = Reseau_social_team.objects.all()
#     serializer_class = Reseau_social_teamSerializer
   
# class TestimonialViewSet(viewsets.ModelViewSet):
#     queryset = Testimonial.objects.all()
#     serializer_class = TestimonialSerializer
   