from rest_framework import serializers
from . models import src


class srcSerializer(serializers.ModelSerializer):
    class Meta:
        model = src
        fields = ('logo_border', 'dominant_color')
