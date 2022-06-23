from rest_framework import viewsets
from serviceConseilApp.serializers import *

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ReseauSocialTeamViewSet(viewsets.ModelViewSet):
    queryset = Reseau_social_team.objects.all()
    serializer_class = Reseau_social_teamSerializer
   
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
   