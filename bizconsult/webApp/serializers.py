from rest_framework import serializers

from webApp import models 


class WebappSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Site_info
        fields = '__all__'

    class Meta:
        model = models.Social_Network
        fields = '__all__'

    class Meta:
        model = models.About
        fields = '__all__'

    class Meta:
        model = models.Contact
        fields = '__all__'

    class Meta:
        model = models.Potentialite
        fields = '__all__'

    class Meta:
        model = models.Feature
        fields = '__all__'

    class Meta:
        model = models.Banner
        fields = '__all__'
