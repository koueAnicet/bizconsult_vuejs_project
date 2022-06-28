from rest_framework import serializers
from serviceConseilApp.models import* 

class ServiceSerializer(serializers.ModelSerializer):

    class  Meta:
        model = Service
        fields= '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Team
        fields= '__all__'

class Reseau_social_teamSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Reseau_social_team
        fields= '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Testimonial
        fields= '__all__'