from rest_framework import viewsets
from webApp.serializers import WebappSerializer
from webApp import models

class SiteInfoViewSet(viewsets.ModelViewSet):
    queryset = models.Site_info.objects.all()
    serializer_class = WebappSerializer

class Social_NetworkViewSet(viewsets.ModelViewSet):
    queryset = models.Social_Network.objects.all()
    serializer_class = WebappSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = WebappSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = models.Feature.objects.all()
    serializer_class = WebappSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = WebappSerializer

class PotentialiteViewiewSet(viewsets.ModelViewSet):
    queryset = models.Potentialite.objects.all()
    serializer_class = WebappSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = models.Banner.objects.all()
    serializer_class = WebappSerializer