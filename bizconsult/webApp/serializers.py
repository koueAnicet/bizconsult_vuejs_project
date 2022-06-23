from rest_framework import serializers

from webApp.models import* 
#from serviceConseilApp.models import* 


class SiteInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site_info
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'

class SocialNetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Social_Network
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

class PotentialiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Potentialite
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

#--------pour le app serviceconseil------ 


# class ServiceSerializer(serializers.ModelSerializer):

#     class  Meta:
#         model = Service
#         fields= '__all__'

# class TeamSerializer(serializers.ModelSerializer):
#     class  Meta:
#         model = Team
#         fields= '__all__'

# class Reseau_social_teamSerializer(serializers.ModelSerializer):
#     class  Meta:
#         model = Reseau_social_team
#         fields= '__all__'

# class TestimonialSerializer(serializers.ModelSerializer):
#     class  Meta:
#         model = Testimonial
#         fields= '__all__'
    

   

