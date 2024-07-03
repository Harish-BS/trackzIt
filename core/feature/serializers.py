from rest_framework import serializers
from core.feature.models import feature

class featureSerializer(serializers.ModelSerializer):
    class Meta:
        model = feature
        fields = '__all__'